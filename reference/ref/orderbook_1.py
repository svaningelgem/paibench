import heapq


def match(orders):
    books = {"buy": [], "sell": []}  # heaps of (key, arrival, qty), best first
    trades = []
    for i, (side, price, qty) in enumerate(orders):
        sign = -1 if side == "buy" else 1  # buy keys are -price: highest bid pops first
        other = books["sell" if side == "buy" else "buy"]
        left = qty
        while left and other and other[0][0] <= -sign * price:
            key, j, size = heapq.heappop(other)
            fill = min(left, size)
            trades.append(
                (i, j, abs(key), fill) if side == "buy" else (j, i, abs(key), fill)
            )
            left -= fill
            if size > fill:
                heapq.heappush(other, (key, j, size - fill))
        if left:
            heapq.heappush(books[side], (sign * price, i, left))
    return trades
