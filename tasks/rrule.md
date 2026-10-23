Write a Python function `occurrences(rule: str, start: str, limit: int) -> list[str]` that expands an iCalendar recurrence rule (RFC 5545 `RRULE`) and returns its first `limit` occurrences as `YYYY-MM-DD` strings, in order; fewer if the rule ends sooner.

- `start` is the DTSTART, a date `YYYY-MM-DD`; there are no times anywhere. `start` is an occurrence only if it matches the rule, and nothing before it is.
- `rule` looks like `FREQ=MONTHLY;BYDAY=-1FR;COUNT=3` and uses only these parts: `FREQ` (`DAILY`, `WEEKLY`, `MONTHLY` or `YEARLY`), `INTERVAL`, `COUNT`, `UNTIL` (a date `YYYYMMDD`), `BYMONTH`, `BYMONTHDAY`, `BYDAY`, `BYSETPOS` and `WKST`.
- Everything else follows RFC 5545.

Use only the standard library. Reply with only the Python code.
