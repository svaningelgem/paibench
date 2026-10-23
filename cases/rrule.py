CASES = [
    (
        "occurrences('FREQ=DAILY;COUNT=3', '2024-02-28', 10)",
        ["2024-02-28", "2024-02-29", "2024-03-01"],
    ),
    (
        "occurrences('FREQ=DAILY;INTERVAL=10;BYMONTH=3', '2024-02-01', 5)",
        ["2024-03-02", "2024-03-12", "2024-03-22", "2025-03-07", "2025-03-17"],
    ),
    (
        "occurrences('FREQ=DAILY;BYDAY=SA,SU;UNTIL=20240115', '2024-01-01', 10)",
        ["2024-01-06", "2024-01-07", "2024-01-13", "2024-01-14"],
    ),
    (
        "occurrences('FREQ=DAILY;BYMONTHDAY=1,15;BYMONTH=6', '2024-01-01', 3)",
        ["2024-06-01", "2024-06-15", "2025-06-01"],
    ),
    (
        "occurrences('FREQ=WEEKLY;BYDAY=WE', '2024-01-01', 3)",
        ["2024-01-03", "2024-01-10", "2024-01-17"],
    ),
    (
        "occurrences('FREQ=WEEKLY;INTERVAL=2;COUNT=4;BYDAY=TU,SU;WKST=MO', '1997-08-05', 10)",
        ["1997-08-05", "1997-08-10", "1997-08-19", "1997-08-24"],
    ),
    (
        "occurrences('FREQ=WEEKLY;INTERVAL=2;COUNT=4;BYDAY=TU,SU;WKST=SU', '1997-08-05', 10)",
        ["1997-08-05", "1997-08-17", "1997-08-19", "1997-08-31"],
    ),
    (
        "occurrences('FREQ=WEEKLY;BYDAY=MO,WE,FR;UNTIL=20240112', '2024-01-01', 10)",
        [
            "2024-01-01",
            "2024-01-03",
            "2024-01-05",
            "2024-01-08",
            "2024-01-10",
            "2024-01-12",
        ],
    ),
    (
        "occurrences('FREQ=WEEKLY;INTERVAL=2;BYDAY=MO', '2024-01-03', 3)",
        ["2024-01-15", "2024-01-29", "2024-02-12"],
    ),
    (
        "occurrences('FREQ=WEEKLY;INTERVAL=3;BYMONTH=12', '2024-10-31', 3)",
        ["2024-12-12", "2025-12-04", "2025-12-25"],
    ),
    (
        "occurrences('FREQ=MONTHLY', '2024-01-31', 5)",
        ["2024-01-31", "2024-03-31", "2024-05-31", "2024-07-31", "2024-08-31"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYMONTHDAY=-1', '2024-01-15', 4)",
        ["2024-01-31", "2024-02-29", "2024-03-31", "2024-04-30"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYMONTHDAY=1,-1', '2024-01-15', 4)",
        ["2024-01-31", "2024-02-01", "2024-02-29", "2024-03-01"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYMONTHDAY=-3', '2023-02-01', 3)",
        ["2023-02-26", "2023-03-29", "2023-04-28"],
    ),
    (
        "occurrences('FREQ=MONTHLY;COUNT=2;BYMONTHDAY=31', '2024-04-01', 10)",
        ["2024-05-31", "2024-07-31"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=-1FR', '2024-01-01', 3)",
        ["2024-01-26", "2024-02-23", "2024-03-29"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=2TU;INTERVAL=3', '2024-01-01', 3)",
        ["2024-01-09", "2024-04-09", "2024-07-09"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=5MO', '2024-01-01', 4)",
        ["2024-01-29", "2024-04-29", "2024-07-29", "2024-09-30"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=FR;BYMONTHDAY=13', '2024-01-01', 3)",
        ["2024-09-13", "2024-12-13", "2025-06-13"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-1', '2024-01-01', 4)",
        ["2024-01-31", "2024-02-29", "2024-03-29", "2024-04-30"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=1,-1', '2024-06-01', 4)",
        ["2024-06-03", "2024-06-28", "2024-07-01", "2024-07-31"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=SA,SU;BYSETPOS=2', '2024-01-01', 3)",
        ["2024-01-07", "2024-02-04", "2024-03-03"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=TU,WE,TH;BYSETPOS=3;COUNT=3', '1997-09-04', 10)",
        ["1997-09-04", "1997-10-07", "1997-11-06"],
    ),
    (
        "occurrences('FREQ=MONTHLY;BYDAY=MO;BYSETPOS=5', '2024-01-01', 3)",
        ["2024-01-29", "2024-04-29", "2024-07-29"],
    ),
    (
        "occurrences('FREQ=MONTHLY;INTERVAL=2;BYMONTH=1,2,3;BYMONTHDAY=-1', '2023-12-15', 3)",
        ["2024-02-29", "2025-02-28", "2026-02-28"],
    ),
    (
        "occurrences('FREQ=YEARLY', '2024-02-29', 3)",
        ["2024-02-29", "2028-02-29", "2032-02-29"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYMONTH=1,7', '2024-03-15', 3)",
        ["2024-07-15", "2025-01-15", "2025-07-15"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYMONTH=2;BYMONTHDAY=29', '2025-01-01', 2)",
        ["2028-02-29", "2032-02-29"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYMONTH=11;BYDAY=4TH', '2024-01-01', 3)",
        ["2024-11-28", "2025-11-27", "2026-11-26"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU', '2024-11-01', 2)",
        ["2025-10-26", "2026-10-25"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYDAY=20MO', '2024-01-01', 2)",
        ["2024-05-13", "2025-05-19"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYDAY=1MO,-1FR', '2024-01-01', 4)",
        ["2024-01-01", "2024-12-27", "2025-01-06", "2025-12-26"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYDAY=FR;BYMONTHDAY=13', '2024-01-01', 3)",
        ["2024-09-13", "2024-12-13", "2025-06-13"],
    ),
    (
        "occurrences('FREQ=YEARLY;INTERVAL=2;BYMONTH=3;BYDAY=SU;COUNT=6', '2024-01-01', 10)",
        [
            "2024-03-03",
            "2024-03-10",
            "2024-03-17",
            "2024-03-24",
            "2024-03-31",
            "2026-03-01",
        ],
    ),
    (
        "occurrences('FREQ=YEARLY;BYMONTH=11;BYDAY=TU;BYMONTHDAY=2,3,4,5,6,7,8;INTERVAL=4', '1996-11-05', 3)",
        ["1996-11-05", "2000-11-07", "2004-11-02"],
    ),
    (
        "occurrences('FREQ=YEARLY;BYDAY=MO,TU,WE,TH,FR;BYSETPOS=-1;BYMONTH=12', '2024-01-01', 3)",
        ["2024-12-31", "2025-12-31", "2026-12-31"],
    ),
]
