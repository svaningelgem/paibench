CASES = [
    ("shifts([0, 0, 1], [2, 2, 2], [1, 0, 2])", [3, 1, 1, 2]),
    ("shifts([0, 1, 2, 3], [3, 3, 3, 3], [0, 1, 2, 3])", [6, 3, 1, 0, 0]),
    (
        "shifts([0, 0, 1, 1, 2, 2, 4, 4], [4, 4, 5, 5, 6, 7, 7, 7], [4, 7, 6, 2, 1, 5, 3, 0])",
        [17, 13, 10, 11, 7, 3, 6, 10, 14],
    ),
    (
        "shifts([0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 4, 7, 10, 10, 11], [3, 3, 7, 7, 10, 10, 10, 10, 11, 11, 12, 13, 14, 14, 14], [14, 12, 8, 2, 7, 10, 5, 4, 11, 1, 3, 6, 13, 0, 9])",
        [44, 41, 37, 29, 22, 16, 12, 11, 16, 20, 21, 27, 35, 39, 42, 49],
    ),
    (
        "shifts([0, 0, 1, 1, 3, 3], [4, 4, 4, 4, 5, 5], [2, 1, 0, 4, 3, 5])",
        [11, 8, 4, 4, 2, 5, 7],
    ),
    ("shifts([0, 0, 0, 0, 2], [1, 4, 4, 4, 4], [0, 3, 4, 2, 1])", [7, 6, 4, 2, 4, 8]),
    ("shifts([0, 0, 2, 2, 3], [2, 3, 3, 4, 4], [3, 2, 1, 0, 4])", [6, 4, 5, 2, 2, 3]),
    ("shifts([0, 0, 0, 0], [1, 1, 2, 3], [2, 3, 0, 1])", [1, 3, 6, 5, 6]),
    (
        "shifts([0, 0, 1, 1, 2, 3, 6], [4, 4, 4, 5, 5, 6, 6], [5, 1, 6, 2, 0, 4, 3])",
        [13, 10, 6, 6, 3, 3, 4, 8],
    ),
    ("shifts([0, 1, 1, 2, 3], [2, 2, 3, 4, 4], [3, 0, 4, 1, 2])", [5, 3, 1, 2, 1, 3]),
    ("shifts([0, 0, 1], [1, 2, 2], [2, 0, 1])", [2, 1, 0, 2]),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(r.randint(0, i) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(r.randint(i, n - 1) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(1), 20000)))).encode()).hexdigest()[:16]",
        "89445132b93f6b78",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 5)) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(min(n - 1, i + r.randint(0, 5)) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(2), 20000)))).encode()).hexdigest()[:16]",
        "54c456b441c303ac",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 300)) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(min(n - 1, i + r.randint(0, 2000)) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(3), 20000)))).encode()).hexdigest()[:16]",
        "9d896e121bdbb6d4",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([0] * n, [n - 1] * n, r.sample(range(n), n)))(__import__('random').Random(4), 20000)))).encode()).hexdigest()[:16]",
        "c627377e9cac539a",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(r.randint(0, i) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(r.randint(i, n - 1) for i in range(n)))], list(range(n))))(__import__('random').Random(5), 20000)))).encode()).hexdigest()[:16]",
        "c570ccf33ede525f",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 50)) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(min(n - 1, i + r.randint(0, 50)) for i in range(n)))], list(range(n - 1, -1, -1))))(__import__('random').Random(6), 20000)))).encode()).hexdigest()[:16]",
        "a73f0b19b0a4493c",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: (list(range(n)), [max(v, i) for i, v in enumerate(sorted(r.randint(i, n - 1) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(7), 20000)))).encode()).hexdigest()[:16]",
        "fa3d31a564488a8d",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 4000)) for i in range(n)))], list(range(n)), r.sample(range(n), n)))(__import__('random').Random(8), 20000)))).encode()).hexdigest()[:16]",
        "0ebb8d58860be3ba",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 20)) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(r.randint(i, n - 1) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(9), 20000)))).encode()).hexdigest()[:16]",
        "1d147a1126bb3a80",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(r.randint(0, i) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(min(n - 1, i + r.randint(0, 1000)) for i in range(n)))], list(range(n - 1, -1, -1))))(__import__('random').Random(10), 20000)))).encode()).hexdigest()[:16]",
        "235fd496929165f7",
    ),
    (
        "__import__('hashlib').sha256(repr(list(shifts(*(lambda r, n: ([min(v, i) for i, v in enumerate(sorted(max(0, i - r.randint(0, 2)) for i in range(n)))], [max(v, i) for i, v in enumerate(sorted(min(n - 1, i + r.randint(0, 2)) for i in range(n)))], r.sample(range(n), n)))(__import__('random').Random(11), 20000)))).encode()).hexdigest()[:16]",
        "54cadbe355e517d7",
    ),
]
