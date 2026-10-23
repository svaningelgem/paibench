CASES = [
    (
        "justify('This is an example of text justification.', 16)",
        ["This    is    an", "example of  text", "justification.  "],
    ),
    (
        "justify('What must be acknowledgment shall be', 16)",
        ["What   must   be", "acknowledgment  ", "shall be        "],
    ),
    ("justify('a b c d e', 8)", ["a b c  d", "e       "]),
    ("justify('aa bb cc dd ee', 13)", ["aa bb  cc  dd", "ee           "]),
    (
        "justify('The quick brown fox jumps over the lazy dog and keeps on running far away', 20)",
        [
            "The quick brown  fox",
            "jumps over the  lazy",
            "dog  and  keeps   on",
            "running far away    ",
        ],
    ),
    (
        "justify('hi abcdefghijk there', 5)",
        ["hi   ", "abcd-", "efgh-", "ijk  ", "there"],
    ),
    ("justify('abcdef', 5)", ["abcd-", "ef   "]),
    ("justify('abcdefghi', 5)", ["abcd-", "efghi"]),
    ("justify('abcdefgh x', 6)", ["abcde-", "fgh x "]),
    ("justify('abcdefgh x yy', 6)", ["abcde-", "fgh  x", "yy    "]),
    ("justify('abcdefghij', 4)", ["abc-", "def-", "ghij"]),
    ("justify('abc d', 2)", ["a-", "bc", "d "]),
    ("justify('ab abcde', 5)", ["ab   ", "abcde"]),
    (
        "justify('one two\\nthree\\n\\n  \\nfour', 9)",
        ["one   two", "three    ", "", "four     "],
    ),
    ("justify('\\n\\n  hello  \\n\\n\\n', 7)", ["hello  "]),
    ("justify('a\\tb\\nc', 5)", ["a b c"]),
    ("justify('aa bb\\r\\n\\r\\ncc', 5)", ["aa bb", "", "cc   "]),
    ("justify('', 5)", []),
    ("justify('  \\n \\t\\n', 5)", []),
]
