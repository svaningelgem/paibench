The function below has bugs. Fix it so it does what its docstring says.

```python
def merge_ranges(ranges):
    """Merge overlapping or touching integer ranges.

    ranges: list of (start, end) tuples, inclusive, start <= end, in any order.
    Returns a new list of merged (start, end) tuples, sorted by start.
    Touching ranges merge too: (1, 3) and (4, 6) become (1, 6).
    The input list must not be modified.
    """
    ranges.sort()
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start < last_end:
            merged[-1] = (last_start, end)
        else:
            merged.append((start, end))
    return merged
```

Reply with only the corrected Python code.
