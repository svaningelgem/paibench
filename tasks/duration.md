Write a Python function `parse_duration(s: str) -> int` that returns the total number of seconds in a duration string such as `"1h30m"` or `"2w 3d"`.

Rules:
- A duration is one or more parts. A part is an integer (digits only, no sign or decimal point) immediately followed by a unit: `w` (week), `d` (day), `h` (hour), `m` (minute), `s` (second).
- Units must appear in that order and each at most once.
- Values may exceed the unit's natural range: `"90m"` is valid.
- Whitespace is allowed between parts and at the start/end, but not inside a part (`"1 h"` is invalid).
- Units are lowercase only.
- Raise `ValueError` for any invalid input, including empty or whitespace-only strings.

Reply with only the Python code.
