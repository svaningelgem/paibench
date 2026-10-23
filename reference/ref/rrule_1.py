import calendar
import re
from datetime import date, timedelta

_DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]


def _ints(value: str) -> list[int]:
    return [int(v) for v in value.split(",")]


def occurrences(rule: str, start: str, limit: int) -> list[str]:
    parts = dict(p.split("=", 1) for p in rule.split(";"))
    freq = parts["FREQ"]
    interval = int(parts.get("INTERVAL", 1))
    count = int(parts.get("COUNT", 0))
    u = parts.get("UNTIL")
    until = date(int(u[:4]), int(u[4:6]), int(u[6:])) if u else date.max
    bymonth = _ints(parts["BYMONTH"]) if "BYMONTH" in parts else []
    bymonthday = _ints(parts["BYMONTHDAY"]) if "BYMONTHDAY" in parts else []
    bysetpos = _ints(parts["BYSETPOS"]) if "BYSETPOS" in parts else []
    byday = []
    for d in parts["BYDAY"].split(",") if "BYDAY" in parts else []:
        n, wd = re.fullmatch(r"([+-]?\d+)?([A-Z]{2})", d).groups()
        byday.append((int(n) if n else 0, _DAYS.index(wd)))
    wkst = _DAYS.index(parts.get("WKST", "MO"))
    dtstart = date.fromisoformat(start)

    if not bymonthday and not byday:
        if freq == "YEARLY":
            bymonth = bymonth or [dtstart.month]
            bymonthday = [dtstart.day]
        elif freq == "MONTHLY":
            bymonthday = [dtstart.day]
        elif freq == "WEEKLY":
            byday = [(0, dtstart.weekday())]

    def matches(d: date, scope: list[date]) -> bool:
        if bymonth and d.month not in bymonth:
            return False
        last = calendar.monthrange(d.year, d.month)[1]
        if bymonthday and not any(md in (d.day, d.day - last - 1) for md in bymonthday):
            return False
        if not byday:
            return True
        for n, wd in byday:
            if d.weekday() != wd:
                continue
            if not n:
                return True
            same = [x for x in scope if x.weekday() == wd]
            if same.index(d) in (n - 1, len(same) + n):
                return True
        return False

    def period(k: int) -> list[date]:
        if freq == "YEARLY":
            year = dtstart.year + k * interval
            first, last = date(year, 1, 1), date(year, 12, 31)
        elif freq == "MONTHLY":
            year, month = divmod(dtstart.month - 1 + k * interval, 12)
            year += dtstart.year
            first = date(year, month + 1, 1)
            last = first.replace(day=calendar.monthrange(year, month + 1)[1])
        elif freq == "WEEKLY":
            first = (
                dtstart
                - timedelta((dtstart.weekday() - wkst) % 7)
                + timedelta(7 * k * interval)
            )
            last = first + timedelta(6)
        else:
            first = last = dtstart + timedelta(k * interval)
        return [first + timedelta(i) for i in range((last - first).days + 1)]

    def in_scope(days: list[date], d: date) -> list[date]:
        if freq == "MONTHLY" or (freq == "YEARLY" and bymonth):
            return [x for x in days if x.month == d.month]
        return days

    result = []
    k = 0
    while len(result) < limit:
        try:
            days = period(k)
        except (ValueError, OverflowError):
            break
        if days[0] > until:
            break
        hits = [d for d in days if matches(d, in_scope(days, d))]
        if bysetpos:
            hits = sorted(
                {
                    hits[p - 1 if p > 0 else p]
                    for p in bysetpos
                    if -len(hits) <= p - (p > 0) < len(hits)
                }
            )
        for d in hits:
            if d < dtstart:
                continue
            if d > until or len(result) == limit:
                return result
            result.append(d.isoformat())
            if len(result) == count:
                return result
        k += 1
    return result
