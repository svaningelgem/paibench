CASES = [
    ("halves([5, 9], [0, 1])", 1),
    ("halves([3, 4, 10], [0, 1, 2])", 2),
    ("halves([1, 2, 3, 4], [0, 0, 1, 1])", 4),
    (
        "halves([1000000000, 1000000000, 1000000000, 1000000000, 1000000000], [0, 0, 0, 0, 0])",
        120,
    ),
    (
        "halves([19, 68, 97, 62, 99, 52, 57, 19, 43, 80, 96], [5, 3, 3, 2, 3, 4, 3, 2, 3, 4, 3])",
        8640,
    ),
    (
        "halves([86, 49, 83, 31, 5, 43, 7, 46, 98, 36, 60, 4, 69, 59], [3, 1, 4, 4, 4, 0, 1, 3, 0, 4, 3, 5, 1, 2])",
        15552,
    ),
    (
        "halves([907139744, 237517128, 852012347, 350549430, 62876062, 196019710, 263351472, 184393437, 281593038, 753973502], [23, 12, 1, 26, 29, 24, 0, 7, 10, 4])",
        1,
    ),
    (
        "halves([341999004, 124274759, 504848722, 624415938, 706808452], [5, 4, 0, 8, 2])",
        1,
    ),
    ("halves([2, 3, 1, 7, 5, 6], [1, 30, 1, 1, 1, 2])", 48),
    ("halves([737443218, 308816043, 230186464], [0, 3, 14])", 1),
    ("halves([13184612, 184469381], [24, 0])", 1),
    (
        "halves(*(lambda r: ([r.randint(1, 10**9) for _ in range(50000)], [r.randint(0, 30) for _ in range(50000)]))(__import__('random').Random(1)))",
        739075690,
    ),
    (
        "halves(*(lambda r: ([r.choice((15, 16)) for _ in range(50000)], [r.randint(0, 3) for _ in range(50000)]))(__import__('random').Random(2)))",
        734256002,
    ),
    (
        "halves(*(lambda r: ([r.randint(1, 8) for _ in range(50000)], [r.randint(0, 3) for _ in range(50000)]))(__import__('random').Random(3)))",
        610275954,
    ),
    (
        "halves(*(lambda r: ([r.choice((2 ** k - 1, 2 ** k)) for k in (r.randint(1, 29) for _ in range(50000))], [r.randint(0, 30) for _ in range(50000)]))(__import__('random').Random(4)))",
        811190908,
    ),
    (
        "halves(*(lambda r: ([r.randint(1000, 1003) for _ in range(50000)], [r.randint(0, 12) for _ in range(50000)]))(__import__('random').Random(5)))",
        587213329,
    ),
    (
        "halves(*(lambda r: ([r.randint(1, 64) for _ in range(50000)], [r.randint(0, 6) for _ in range(50000)]))(__import__('random').Random(6)))",
        639578566,
    ),
    (
        "halves(*(lambda r: ([r.choice((7, 8, 15, 16, 31, 32)) for _ in range(50000)], [r.randint(0, 5) for _ in range(50000)]))(__import__('random').Random(7)))",
        41115274,
    ),
    (
        "halves(*(lambda r: ([r.randint(1, 10**6) for _ in range(49999)], [r.choice((0, 0, 0, 20)) for _ in range(49999)]))(__import__('random').Random(8)))",
        837794777,
    ),
    (
        "halves(*(lambda r: ([r.randint(1, 3) for _ in range(50000)], [r.randint(0, 2) for _ in range(50000)]))(__import__('random').Random(9)))",
        731988280,
    ),
    (
        "halves(*(lambda r: ([r.choice((5, 6, 11, 12, 23, 24, 47, 48)) for _ in range(50000)], [r.randint(0, 7) for _ in range(50000)]))(__import__('random').Random(10)))",
        823863899,
    ),
    (
        "halves(*(lambda r: ([r.randint(10**8, 10**8 + 50) for _ in range(50000)], [r.randint(0, 30) for _ in range(50000)]))(__import__('random').Random(11)))",
        205714251,
    ),
]
