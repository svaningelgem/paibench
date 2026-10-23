"""Score saved model answers.

Layout: <dir>/<model>/<task>_<run>.<ext>, e.g. answers/model-a/calc_3.md
Usage:  python3 score.py answers [-v]
"""

import builtins
import contextlib
import io
import json
import os
import platform
import queue
import re
import runpy
import subprocess
import sys
import threading
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import IO

HERE = Path(__file__).resolve().parent
TASKS = sorted(p.stem for p in (HERE / "cases").glob("*.py"))
# TASKS="calc ring" in the environment scores only those tasks, as run.sh runs only those
if (wanted := os.environ.get("TASKS", "").split()) and wanted != ["all"]:
    TASKS = [t for t in TASKS if t in wanted]
# seconds per case: 10x what a right solution needs on a slow machine, far below brute force
TIMEOUT = 10
# what -I does, plus a fixed hash seed so an answer's set order is the same on every run
CHILD_ENV = {k: v for k, v in os.environ.items() if not k.startswith("PYTHON")} | {
    "PYTHONHASHSEED": "0",
    "PYTHONSAFEPATH": "1",
}


def extract_code(text: str) -> str:
    blocks = re.findall(r"```[\w+-]*\n(.*?)```", text, re.DOTALL)
    return max(blocks, key=len) if blocks else text


def is_exc(want: object) -> bool:
    return isinstance(want, type) and issubclass(want, BaseException)


def same(got: object, want: object) -> bool:
    if isinstance(want, int | float) and isinstance(got, int | float):
        return abs(got - want) <= 1e-9 * max(1, abs(want))
    return got == want


def child(task: str, answer: Path, start: int) -> None:
    """Print "loaded", then per case from `start` one JSON line: null, or why it failed."""
    cases = runpy.run_path(str(HERE / "cases" / f"{task}.py"))["CASES"]
    # eval/exec blocked so calc can't cheat; ast-walking still slips through
    safe = {k: v for k, v in vars(builtins).items() if k not in ("eval", "exec")}
    ns = {"__name__": "answer", "__builtins__": safe}

    def report(result: str | None) -> None:
        print(json.dumps(result), file=sys.__stdout__, flush=True)

    with contextlib.redirect_stdout(io.StringIO()):
        try:
            exec(extract_code(answer.read_text()), ns)  # noqa: S102
        except BaseException as e:  # noqa: BLE001
            report(f"<load error> {e!r}")
            return
        report("loaded")
        for expr, want in cases[start:]:
            try:
                got = eval(expr, ns)
                ok, detail = not is_exc(want) and same(got, want), repr(got)
            except Exception as e:  # noqa: BLE001
                ok, detail = (
                    is_exc(want) and isinstance(e, want),
                    f"{type(e).__name__}: {e}",
                )
            want_name = getattr(want, "__name__", repr(want))
            report(None if ok else f"{expr} -> {detail}, want {want_name}")


def pump(stream: IO[str], lines: queue.Queue) -> None:
    for line in stream:
        lines.put(line)
    lines.put("")  # EOF, which json.loads rejects like a garbled line


def score(task: str, answer: Path) -> dict:
    """A case that hangs or kills the child fails; a new child goes on after it."""
    cases = runpy.run_path(str(HERE / "cases" / f"{task}.py"))["CASES"]
    failed, i = [], 0
    while i < len(cases):
        proc = subprocess.Popen(
            [
                sys.executable,
                "-s",
                str(HERE / "score.py"),
                "--child",
                task,
                str(answer),
                str(i),
            ],
            env=CHILD_ENV,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        lines = queue.Queue()
        threading.Thread(target=pump, args=(proc.stdout, lines), daemon=True).start()
        loaded = False
        try:
            if (first := json.loads(lines.get(timeout=TIMEOUT))) != "loaded":
                return {"score": 0, "failed": [first]}
            loaded = True
            while i < len(cases):
                if result := json.loads(lines.get(timeout=TIMEOUT)):
                    failed.append(result)
                i += 1
        except (queue.Empty, json.JSONDecodeError):
            if not loaded:
                return {"score": 0, "failed": ["<load timeout or crash>"]}
            failed.append(f"{cases[i][0]} -> <timeout or crash>")
            i += 1
        finally:
            proc.kill()
            proc.wait()
    return {"score": 1 - len(failed) / len(cases), "failed": failed}


def main() -> None:
    if sys.argv[1] == "--child":
        child(sys.argv[2], Path(sys.argv[3]), int(sys.argv[4]))
        return
    runs = defaultdict(list)
    for answer in sorted(Path(sys.argv[1]).glob("*/*_*")):
        task = answer.stem.rsplit("_", 1)[0]
        if task not in TASKS:
            continue
        result = score(task, answer)
        runs[answer.parent.name, task].append(result["score"])
        if "-v" in sys.argv and result["failed"]:
            print(f"{answer}:", *result["failed"], sep="\n  ")

    print(f"\n{'model':<16}" + "".join(f"{t:>14}" for t in TASKS) + f"{'overall':>10}")
    for model in sorted({m for m, _ in runs}):
        cells, means = [], []
        for task in TASKS:
            if scores := runs.get((model, task)):
                means.append(mean(scores))
                cells.append(
                    f"{means[-1]:.0%} {sum(s == 1 for s in scores)}/{len(scores)}"
                )
            else:
                cells.append("-")
        print(
            f"{model:<16}"
            + "".join(f"{c:>14}" for c in cells)
            + f"{mean(means):>10.0%}"
        )
    print("\ncell = avg share of test cases passed, then fully-correct runs / runs")
    print(f"scored with Python {platform.python_version()}")


if __name__ == "__main__":
    main()
