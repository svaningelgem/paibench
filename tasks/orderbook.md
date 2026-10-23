The function below has bugs. Fix it so it does what its docstring says.

```python
import heapq


def match(orders):
    """Match limit orders for one instrument and return the trades.

    orders: list of (side, price, qty) tuples in arrival order; side is "buy" or
    "sell", price and qty are positive integers.

    Each incoming order trades against the best resting order on the other side
    for as long as it has quantity left and the prices cross (buy price >= sell
    price). Best means the highest buy or lowest sell price, and the earliest
    arrival among equal prices. A trade happens at the resting order's price.
    Whatever is left of the incoming order then rests in the book, keeping its
    arrival time.

    Returns the trades in the order they happen, as (buy_index, sell_index,
    price, qty) tuples, where the indexes point into orders.
    """
    books = {"buy": [], "sell": []}  # heaps of (key, arrival, qty), best first
    trades = []
    for i, (side, price, qty) in enumerate(orders):
        sign = -1 if side == "buy" else 1  # buy keys are -price: highest bid pops first
        other = books["sell" if side == "buy" else "buy"]
        left = qty
        while left and other and other[0][0] < -sign * price:
            key, j, size = heapq.heappop(other)
            fill = min(left, size)
            trades.append((i, j, price, fill))
            left -= fill
            if size > fill:
                heapq.heappush(other, (key, i, size - fill))
        if left:
            heapq.heappush(books[side], (sign * price, i, qty))
    return trades
```

Reply with only the corrected Python code.
