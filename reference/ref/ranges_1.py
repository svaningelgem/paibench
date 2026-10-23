import re

_NUM = r"0|[1-9][0-9]*"
_PRE = rf"(?:{_NUM}|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
_BUILD = r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
_SEMVER = re.compile(
    rf"({_NUM})\.({_NUM})\.({_NUM})(?:-({_PRE}(?:\.{_PRE})*))?{_BUILD}"
)
_X = rf"{_NUM}|[xX*]"
_PARTIAL = re.compile(
    rf"(<=|>=|<|>|=|~|\^)?({_X})(?:\.({_X})(?:\.({_X})(?:-({_PRE}(?:\.{_PRE})*))?{_BUILD})?)?"
)


def _pre(pre: str | None) -> tuple:
    if not pre:
        return ()
    return tuple((0, int(i), "") if i.isdigit() else (1, 0, i) for i in pre.split("."))


def _key(core: tuple, pre: tuple) -> tuple:
    return core, (0, pre) if pre else (1, ())


def _desugar(token: str) -> list[tuple]:
    op, *parts, pre = _PARTIAL.fullmatch(token).groups()
    nums = [None if p is None or p in "xX*" else int(p) for p in parts]
    if None in nums:
        nums = nums[: nums.index(None)]
    pre = _pre(pre) if len(nums) == 3 else ()
    m = [*nums, 0, 0, 0][:3]
    zero = _pre("0")

    def bump(i: int) -> tuple:
        return (*m[:i], m[i] + 1, *[0] * (2 - i))

    op = op or "="
    if op in "~^" and not nums:
        return []
    if op == "~":
        upper = bump(1) if len(nums) >= 2 else bump(0)
        return [(">=", tuple(m), pre), ("<", upper, zero)]
    if op == "^":
        first = next((i for i in range(len(nums) - 1) if nums[i]), len(nums) - 1)
        return [(">=", tuple(m), pre), ("<", bump(first), zero)]
    if len(nums) == 3:
        return [(op, tuple(m), pre)]
    if not nums:
        return [("<", (0, 0, 0), zero)] if op in ("<", ">") else []
    last = len(nums) - 1
    match op:
        case "=":
            return [(">=", tuple(m), ()), ("<", bump(last), zero)]
        case ">":
            return [(">=", bump(last), ())]
        case ">=":
            return [(">=", tuple(m), ())]
        case "<":
            return [("<", tuple(m), zero)]
        case "<=":
            return [("<", bump(last), zero)]


def _sets(rng: str) -> list[list[tuple]]:
    sets = []
    for part in rng.split("||"):
        if m := re.fullmatch(r"\s*(\S+)\s+-\s+(\S+)\s*", part):
            sets.append(_desugar(">=" + m[1]) + _desugar("<=" + m[2]))
        else:
            sets.append([c for token in part.split() for c in _desugar(token)])
    return sets


def _test(core: tuple, pre: tuple, comparators: list[tuple]) -> bool:
    v = _key(core, pre)
    for op, c_core, c_pre in comparators:
        c = _key(c_core, c_pre)
        ok = {"<": v < c, "<=": v <= c, ">": v > c, ">=": v >= c, "=": v == c}[op]
        if not ok:
            return False
    if not pre:
        return True
    return any(c_pre and c_core == core for _, c_core, c_pre in comparators)


def satisfies(version: str, rng: str) -> bool:
    m = _SEMVER.fullmatch(version)
    if not m:
        raise ValueError(f"invalid version: {version!r}")
    core = tuple(int(g) for g in m.groups()[:3])
    pre = _pre(m.group(4))
    return any(_test(core, pre, s) for s in _sets(rng))
