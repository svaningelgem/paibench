CASES = [
    ("arrows([(4, 1), (5, -1), (3, 2), (-6, 0), (1, 1)])", 4),
    ("arrows([(1, 0), (1, 0), (1, 0), (1, 0)])", 4),
    ("arrows([(0, 0)])", 0),
    ("arrows([(7, -3)])", 0),
    ("arrows([(3, 0), (2, 2), (-1, 1), (0, 4)])", 0),
    ("arrows([(0, -2), (2, 0), (-1, -3), (-1, -2), (-1, 1), (2, 0), (-2, -3)])", 20),
    (
        "arrows([(-5, 44), (-18, 43), (-13, 23), (-39, 46), (-23, 21), (12, 33), (14, 16), (4, 66), (10, 57), (-31, -34)])",
        68630,
    ),
    (
        "arrows([(-8, -5), (-6, -2), (-3, -4), (-6, 3), (6, -1), (-8, -1), (-5, 6), (-6, -2), (-3, 1)])",
        916,
    ),
    (
        "arrows([(4, -15), (-8, -33), (-42, -48), (-8, -40), (-43, 33), (14, -38)])",
        5578,
    ),
    ("arrows([(5, 2), (2, 3), (0, 6), (4, 7)])", 16),
    ("arrows([(48, 50), (40, 41), (15, 31), (44, 51), (20, 12)])", 19058),
    (
        "arrows((lambda r: [(r.randint(-45000, 45000), r.randint(-45000, 45000)) for _ in range(20000)])(__import__('random').Random(1)))",
        51160418727646962,
    ),
    (
        "arrows((lambda r: [(r.randint(-m, m), r.randint(-m, m)) for m in (2 ** r.randint(0, 15) for _ in range(20000))])(__import__('random').Random(2)))",
        405876381099742,
    ),
    (
        "arrows((lambda r: [(x, r.randint(-abs(x) // 8, abs(x) // 8)) for x in (r.randint(-3000, 90000) for _ in range(20000))])(__import__('random').Random(3)))",
        750611403315833950,
    ),
    (
        "arrows((lambda r: [(r.randint(-3, 3), r.randint(-3, 3)) for _ in range(20000)])(__import__('random').Random(4)))",
        300663862,
    ),
    (
        "arrows((lambda r: [(k * dx, k * dy) for dx, dy, k in ((r.randint(-9, 9), r.randint(-9, 9), r.randint(1, 4000)) for _ in range(20000))])(__import__('random').Random(5)))",
        9064832091288330,
    ),
    (
        "arrows((lambda r: [(r.randint(-m, m), r.randint(-m, m)) for m in ((90000 if r.random() < 0.01 else 30) for _ in range(20000))])(__import__('random').Random(6)))",
        20001918226364,
    ),
    (
        "arrows((lambda r: [p for x, y in ((r.randint(-40000, 40000), r.randint(-40000, 40000)) for _ in range(10000)) for p in ((x, y), (-x, -y + r.randint(-5, 5)))])(__import__('random').Random(7)))",
        39863777322119650,
    ),
    (
        "arrows((lambda r: [(r.randint(-20000, 60000), r.randint(-70000, 10000)) for _ in range(20000)])(__import__('random').Random(8)))",
        535506568618703730,
    ),
    (
        "arrows((lambda r: [(r.randint(-m, m), r.randint(-m, m)) for m in (r.choice((1, 10, 100, 1000, 40000)) for _ in range(20000))])(__import__('random').Random(9)))",
        1729282561622446,
    ),
    (
        "arrows((lambda r: [(x + r.randint(-60, 60), y + r.randint(-60, 60)) for x, y in (r.choice(((3000, 0), (0, 3000), (-2500, -2500))) for _ in range(20000))])(__import__('random').Random(10)))",
        796508422380248,
    ),
    (
        "arrows((lambda r: [(r.randint(1, 45000), r.randint(-45000, 45000)) for _ in range(20000)])(__import__('random').Random(11)))",
        202563743306603904,
    ),
]
