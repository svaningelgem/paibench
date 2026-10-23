CASES = [
    ("records(4, '110110')", 1),
    ("records(2, '1')", 0),
    ("records(3, '000')", 0),
    ("records(5, '1111111110')", 3),
    ("records(3, '011')", 0),
    ("records(4, '111110')", 2),
    (
        "records(6, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(0, m), 4))))(__import__('random').Random(137288), 15))",
        1,
    ),
    (
        "records(7, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(13, m), 8))))(__import__('random').Random(577359), 21))",
        6,
    ),
    (
        "records(8, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(0, m), 5))))(__import__('random').Random(682851), 28))",
        1,
    ),
    (
        "records(8, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(16, m), 7))))(__import__('random').Random(418557), 28))",
        0,
    ),
    (
        "records(9, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(16, m), 11))))(__import__('random').Random(683341), 36))",
        4,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(10775, m), 8))))(__import__('random').Random(890377), 11175))",
        324,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(10775, m), 132))))(__import__('random').Random(537867), 11175))",
        39,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(9175, m), 11))))(__import__('random').Random(263268), 11175))",
        185,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(10875, m), 275))))(__import__('random').Random(78849), 11175))",
        487,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(10875, m), 241))))(__import__('random').Random(732077), 11175))",
        802,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(0, m), 100))))(__import__('random').Random(503347), 11175))",
        3,
    ),
    (
        "records(120, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(6740, m), 29))))(__import__('random').Random(978733), 7140))",
        343,
    ),
    (
        "records(100, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(0, m), 64))))(__import__('random').Random(997657), 4950))",
        0,
    ),
    (
        "records(150, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(10775, m), 102))))(__import__('random').Random(194855), 11175))",
        419,
    ),
    (
        "records(140, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(9430, m), 201))))(__import__('random').Random(852588), 9730))",
        51,
    ),
    (
        "records(130, (lambda r, m: (lambda zeros: ''.join('0' if i in zeros else '1' for i in range(m)))(set(r.sample(range(6885, m), 23))))(__import__('random').Random(462247), 8385))",
        164,
    ),
]
