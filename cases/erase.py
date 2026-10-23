CASES = [
    ("erase('baabaa', [(0, 6), (3, 5), (2, 5), (1, 3), (2, 4)])", [2, 0, 1, 2, -1]),
    ("erase('ab', [(0, 2), (0, 1), (1, 2)])", [-1, 1, 1]),
    ("erase('bbaa', [(0, 4), (1, 3), (0, 3)])", [0, 0, 1]),
    ("erase('aabb', [(0, 4), (1, 3)])", [-1, -1]),
    (
        "erase('aba', [(0, 2), (1, 2), (1, 2), (2, 3), (2, 3), (0, 2)])",
        [-1, 1, 1, 1, 1, -1],
    ),
    ("erase('ababbbbb', [(2, 4), (0, 2), (0, 2), (0, 5)])", [-1, -1, -1, -1]),
    (
        "erase('a', [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)])",
        [1, 1, 1, 1, 1, 1],
    ),
    (
        "erase('aabab', [(3, 5), (1, 2), (3, 5), (0, 4), (2, 3), (3, 4)])",
        [-1, 1, -1, 2, 1, 1],
    ),
    (
        "erase('babb', [(1, 3), (0, 1), (0, 1), (0, 4), (2, 4), (1, 2)])",
        [-1, 1, 1, 2, 2, 1],
    ),
    ("erase('aababbbbbaba', [(2, 8), (2, 4), (6, 11), (6, 11)])", [4, 0, 3, 3]),
    (
        "erase('aaa', [(0, 1), (0, 1), (1, 2), (0, 1), (1, 2), (2, 3), (1, 3), (2, 3)])",
        [1, 1, 1, 1, 1, 1, 2, 1],
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(1), 100000, 10000, 0.5)))).encode()).hexdigest()[:16]",
        "ff62dd85008aa39f",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(2), 100000, 10000, 0.55)))).encode()).hexdigest()[:16]",
        "87109eefae95f9ed",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(3), 100000, 10000, 0.45)))).encode()).hexdigest()[:16]",
        "7f8b8782439fa08b",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(4), 100000, 10000, 0.7)))).encode()).hexdigest()[:16]",
        "731614b2783d1990",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(5), 100000, 10000, 0.3)))).encode()).hexdigest()[:16]",
        "a70c244ee406abda",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(6), 100000, 10000, 0.51)))).encode()).hexdigest()[:16]",
        "9a55e49b4bffdea4",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(__import__('random').Random(7), 100000, 10000, ('bbbaabbbbaabbbbaabaab' * 100000)[:100000])))).encode()).hexdigest()[:16]",
        "77dd6f71107338af",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(__import__('random').Random(8), 100000, 10000, ('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' * 100000)[:100000])))).encode()).hexdigest()[:16]",
        "05149ae173bafa1f",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(9), 100000, 10000, 0.6)))).encode()).hexdigest()[:16]",
        "36c3b9b299ec8cba",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, p: (lambda s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(''.join('b' if r.random() < p else 'a' for _ in range(n))))(__import__('random').Random(10), 100000, 10000, 0.49)))).encode()).hexdigest()[:16]",
        "9b1fbe41a0e606cf",
    ),
    (
        "__import__('hashlib').sha256(repr(list(erase(*(lambda r, n, q, s: (s, [tuple(sorted(r.sample(range(n + 1), 2))) for _ in range(q)]))(__import__('random').Random(11), 100000, 10000, ('bababababababababababababababababababababababababababababababababababababababababbabbabbabbabbabbabbaaaaaaaaaa' * 100000)[:100000])))).encode()).hexdigest()[:16]",
        "1ab4c0be7e47d2b1",
    ),
]
