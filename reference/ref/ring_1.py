def after(state: str, offsets: list[int], t: int) -> str:
    n = len(state)
    mask = (1 << n) - 1
    lamps = int(state[::-1], 2)  # bit i is lamp i

    def rotate(bits: int, s: int) -> int:  # bit i of the result is bit (i + s) % n
        return ((bits >> s) | (bits << (n - s))) & mask

    # over GF(2), applying the step 2**j times is the same step with every offset times 2**j
    shifts = [o % n for o in offsets]
    while t:
        if t & 1:
            new = 0
            for s in shifts:
                new ^= rotate(lamps, s)
            lamps = new
        shifts = [2 * s % n for s in shifts]
        t >>= 1
    return format(lamps, f"0{n}b")[::-1]
