CASES = [
    ("fewest(3, [(0, 1)], [1, 2, 3])", 1),
    ("fewest(1, [], [1])", 0),
    ("fewest(4, [], [4, 2, 1, 3])", 3),
    ("fewest(4, [(0, 1), (1, 2), (2, 3)], [1, 2, 3, 4])", 0),
    (
        "fewest(7, [(1, 3), (3, 2), (0, 2), (5, 2), (1, 6), (5, 0)], [4, 2, 7, 5, 3, 1, 6])",
        4,
    ),
    ("fewest(2, [], [2, 1])", 1),
    (
        "fewest(7, [(5, 1), (2, 5), (0, 1), (3, 6), (3, 1), (3, 4), (6, 4), (2, 4), (0, 5), (3, 0), (6, 2), (3, 2), (4, 1), (0, 4), (0, 6), (6, 1), (5, 4), (3, 5), (6, 5), (2, 1), (0, 2)], [2, 7, 4, 1, 6, 5, 3])",
        0,
    ),
    ("fewest(2, [], [2, 1])", 1),
    (
        "fewest(7, [(5, 1), (6, 3), (0, 2), (0, 4), (1, 2), (1, 6), (6, 0), (1, 0), (3, 0), (1, 3), (6, 2)], [5, 2, 6, 4, 7, 1, 3])",
        1,
    ),
    ("fewest(1, [], [1])", 0),
    ("fewest(1, [], [1])", 0),
    ("fewest(5, [(3, 2), (0, 2)], [3, 5, 4, 1, 2])", 3),
    ("fewest(3, [(0, 1), (0, 2), (2, 1)], [1, 3, 2])", 0),
    ("fewest(2, [(1, 0)], [2, 1])", 0),
    ("fewest(4, [(0, 3), (1, 3), (0, 1)], [2, 3, 1, 4])", 1),
    ("fewest(5, [(1, 0), (4, 0), (2, 0), (1, 4), (3, 2)], [5, 2, 4, 1, 3])", 2),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(1), 200000, 200000, 1)",
        73341,
    ),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(2), 200000, 200000, 3)",
        113133,
    ),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(3), 150000, 200000, 20)",
        119314,
    ),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(4), 200000, 100000, 2)",
        132933,
    ),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(5), 100000, 200000, 1000)",
        96417,
    ),
    (
        "(lambda r, n, m, span: (lambda who: fewest(n, list({(who[i], who[min(n - 1, i + 1 + r.randrange(span))]) for i in (r.randrange(n - 1) for _ in range(m))}), [p for _, p in sorted(zip(who, range(1, n + 1)))]))(r.sample(range(n), n)))(__import__('random').Random(6), 200000, 150000, 5)",
        139920,
    ),
]
