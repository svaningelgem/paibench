def transform(grid: list[str]) -> list[str]:
    h, w = len(grid), len(grid[0])
    out = [list(row) for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != "." or (r, c) in seen:
                continue
            seen.add((r, c))
            region, todo, border = [], [(r, c)], False
            while todo:
                y, x = todo.pop()
                region.append((y, x))
                border |= y in (0, h - 1) or x in (0, w - 1)
                for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if (
                        0 <= ny < h
                        and 0 <= nx < w
                        and grid[ny][nx] == "."
                        and (ny, nx) not in seen
                    ):
                        seen.add((ny, nx))
                        todo.append((ny, nx))
            if not border:
                mark = str(len(region)) if len(region) <= 9 else "+"
                for y, x in region:
                    out[y][x] = mark
    return ["".join(row) for row in out]
