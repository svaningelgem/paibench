from math import acos, atan2, pi, sqrt


def arrows(points: list[tuple[int, int]]) -> int:
    best = 0
    norms = [x * x + y * y for x, y in points]
    angles = [atan2(y, x) for x, y in points]
    # an arrow of length up to `reach` joins the subset while the direction is within acos(len / reach) of it
    for bit in range(31):
        reach = 1 << bit
        sx = sy = base = 0
        events = []
        for i, (x, y) in enumerate(points):
            ratio = sqrt(norms[i]) / reach
            if ratio > 1:
                continue
            spread = acos(ratio)
            lo, hi = (angles[i] - spread) % (2 * pi), (angles[i] + spread) % (2 * pi)
            if lo > hi:
                sx, sy, base = sx + x, sy + y, base - 3 * norms[i]
            events.append((lo, -1, i))
            events.append((hi, 1, i))
        events.sort()
        best = max(best, base + sx * sx + sy * sy)
        for _, leave, i in events:
            x, y = points[i]
            sx, sy, base = sx + leave * -x, sy + leave * -y, base + leave * 3 * norms[i]
            best = max(best, base + sx * sx + sy * sy)
    return best
