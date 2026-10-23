import re

_TOKEN = re.compile(r"\s*(?:(\d+(?:\.\d+)?)|([A-Z]+\d*)|(<>|<=|>=|[-+*/=<>(),:]))")
_REF = re.compile(r"[A-Z][1-9]\d?")
_CMP = {
    "=": float.__eq__,
    "<>": float.__ne__,
    "<": float.__lt__,
    "<=": float.__le__,
    ">": float.__gt__,
    ">=": float.__ge__,
}


class _Err(str):
    pass


SYNTAX, VALUE, DIV0, CYCLE = map(_Err, ("#SYNTAX!", "#VALUE!", "#DIV/0!", "#CYCLE!"))


def _tokenize(src: str) -> list[str]:
    tokens, pos = [], 0
    while src[pos:].strip():
        m = _TOKEN.match(src, pos)
        if not m:
            raise SyntaxError
        tokens.append(m.group().strip())
        pos = m.end()
    return tokens


def _parse(src: str):
    tokens = _tokenize(src)
    pos = 0

    def peek(k: int = 0) -> str:
        return tokens[pos + k] if pos + k < len(tokens) else ""

    def take(expected: str | None = None) -> str:
        nonlocal pos
        tok = peek()
        if not tok or (expected and tok != expected):
            raise SyntaxError
        pos += 1
        return tok

    def binary(sub, ops):
        def parse():
            node = sub()
            while peek() in ops:
                node = ("bin", take(), node, sub())
            return node

        return parse

    def unary():
        if peek() == "-":
            take()
            return ("neg", unary())
        return primary()

    def primary():
        tok = take()
        if tok[0].isdigit():
            return ("num", float(tok))
        if tok == "(":
            node = expr()
            take(")")
            return node
        if _REF.fullmatch(tok):
            return ("ref", tok)
        if tok == "IF":
            take("(")
            cond = expr()
            take(",")
            then = expr()
            take(",")
            other = expr()
            take(")")
            return ("if", cond, then, other)
        if tok in ("SUM", "MIN", "MAX"):
            take("(")
            args = [argument()]
            while peek() == ",":
                take()
                args.append(argument())
            take(")")
            return ("fn", tok, args)
        raise SyntaxError

    def argument():
        if _REF.fullmatch(peek()) and peek(1) == ":":
            a, _, b = take(), take(), take()
            if not _REF.fullmatch(b):
                raise SyntaxError
            return ("cells", _rect(a, b))
        if _REF.fullmatch(peek()) and peek(1) in (",", ")"):
            return ("cells", [take()])
        return expr()

    expr = binary(binary(binary(unary, ("*", "/")), ("+", "-")), tuple(_CMP))
    node = expr()
    if pos != len(tokens):
        raise SyntaxError
    return node


def _rect(a: str, b: str) -> list[str]:
    cols = sorted((a[0], b[0]))
    rows = sorted((int(a[1:]), int(b[1:])))
    return [
        f"{chr(c)}{r}"
        for r in range(rows[0], rows[1] + 1)
        for c in range(ord(cols[0]), ord(cols[1]) + 1)
    ]


def evaluate(cells: dict[str, str]) -> dict[str, float | str]:
    values: dict[str, float | str] = {}
    busy: set[str] = set()

    def cell(name: str) -> float | str:
        if name not in cells:
            return 0.0
        if name in values:
            return values[name]
        if name in busy:
            return CYCLE
        raw = cells[name]
        if re.fullmatch(r"-?\d+(\.\d+)?", raw):
            value = float(raw)
        elif raw.startswith("="):
            try:
                node = _parse(raw[1:])
            except SyntaxError:
                value = SYNTAX
            else:
                busy.add(name)
                value = ev(node)
                busy.discard(name)
        else:
            value = raw
        values[name] = value
        return value

    def number(node) -> float | _Err:
        v = ev(node)
        if isinstance(v, _Err):
            return v
        return VALUE if isinstance(v, str) else v

    def ev(node) -> float | str:
        match node:
            case ("num", v):
                return v
            case ("ref", name):
                return cell(name)
            case ("neg", sub):
                v = number(sub)
                return v if isinstance(v, _Err) else -v
            case ("bin", op, left, right):
                a = number(left)
                if isinstance(a, _Err):
                    return a
                b = number(right)
                if isinstance(b, _Err):
                    return b
                if op in _CMP:
                    return float(_CMP[op](a, b))
                if op == "/":
                    return DIV0 if b == 0 else a / b
                return a + b if op == "+" else a - b if op == "-" else a * b
            case ("if", cond, then, other):
                c = number(cond)
                if isinstance(c, _Err):
                    return c
                return ev(then if c != 0 else other)
            case ("fn", fn, args):
                nums = []
                for arg in args:
                    if arg[0] == "cells":
                        for name in arg[1]:
                            v = cell(name) if name in cells else ""
                            if isinstance(v, _Err):
                                return v
                            if not isinstance(v, str):
                                nums.append(v)
                    else:
                        v = number(arg)
                        if isinstance(v, _Err):
                            return v
                        nums.append(v)
                if fn == "SUM":
                    return float(sum(nums))
                return (min if fn == "MIN" else max)(nums, default=0.0)

    return {
        name: v if not isinstance(v, _Err) else str(v)
        for name in cells
        for v in [cell(name)]
    }
