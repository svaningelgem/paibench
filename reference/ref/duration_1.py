import re

_PATTERN = re.compile(r"\s*".join(rf"(?:([0-9]+){u})?" for u in "wdhms"))
_SECONDS = (604800, 86400, 3600, 60, 1)


def parse_duration(s: str) -> int:
    m = _PATTERN.fullmatch(s.strip())
    if not m or not any(m.groups()):
        raise ValueError(f"invalid duration: {s!r}")
    return sum(int(v) * k for v, k in zip(m.groups(), _SECONDS) if v)
