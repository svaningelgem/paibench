import re


def calc(expr: str) -> float:
    tokens = re.findall(r"[0-9]*\.?[0-9]+|\S", expr)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def take():
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError("unexpected end of input")
        pos += 1
        return tokens[pos - 1]

    def expression():
        value = term()
        while peek() in ("+", "-"):
            value = value + term() if take() == "+" else value - term()
        return value

    def term():
        value = factor()
        while peek() in ("*", "/"):
            value = value * factor() if take() == "*" else value / factor()
        return value

    def factor():
        if peek() in ("+", "-"):
            return -factor() if take() == "-" else factor()
        base = primary()
        if peek() == "^":
            take()
            return base ** factor()
        return base

    def primary():
        tok = take()
        if tok == "(":
            value = expression()
            if take() != ")":
                raise ValueError("expected ')'")
            return value
        if tok[0] in "0123456789.":
            return float(tok)
        raise ValueError(f"unexpected {tok!r}")

    value = expression()
    if pos != len(tokens):
        raise ValueError(f"unexpected {tokens[pos]!r}")
    return value
