# paibench

A small, cheap way to compare the coding skills of LLMs. Each of the four tasks is a short prompt, and the
reply is scored against hidden test cases. That gives a percentage instead of a pass/fail, and it costs few
enough tokens to run every task 5 times per model. Scoring needs only the Python standard library.

| Task | Measures | Cases |
|---|---|---|
| `duration` | following a spec, input validation | 24 |
| `bugfix` | reading code, finding the bugs | 13 |
| `calc` | parsing, precedence and associativity | 36 |
| `semver` | precise spec knowledge, edge cases | 39 |

## Usage

1. For each model, task and run (1-5): open a **fresh chat**, paste `tasks/<task>.md`, and save the whole
   reply as `answers/<model>/<task>_<run>.md`.
   - Keep the model's normal sampling settings. At temperature 0 the 5 runs come out identical.
   - Run agents (IDE assistants, CLI agents) in an empty folder, not in this repo, or they can read the
     cases and reference answers.
2. `python3 score.py answers`, add `-v` to see which cases failed:

```
model                   bugfix          calc      duration        semver   overall
model-a               100% 5/5       94% 2/5      100% 5/5       85% 1/5       95%
```

A cell like `94% 2/5` means 94% of cases passed on average, and 2 of the 5 runs were fully correct.

`answers/` is git-ignored, so your results stay local.

## Self-check

`python3 score.py reference` must show 100% everywhere.

Answers run as plain Python on your machine, each in its own process with a 10 s timeout and `eval`/`exec`
disabled. Only score replies you are willing to execute.
