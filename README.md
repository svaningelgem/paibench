# paibench

A small, cheap way to compare the coding skills of LLMs. Each task is a short prompt, and the reply is
scored against hidden test cases. That gives a percentage instead of a pass/fail, and it costs few enough
tokens to run every task 5 times per model. Scoring needs only the Python standard library.

| Task | Measures | Cases |
|---|---|---|
| `duration` | following a spec, input validation | 24 |
| `bugfix` | reading code, finding the bugs | 13 |
| `calc` | parsing, precedence and associativity | 36 |
| `semver` | precise spec knowledge, edge cases | 39 |
| `ranges` | npm semver ranges: caret on `0.x`, partial versions, the prerelease rule | 70 |
| `rrule` | RFC 5545 recurrence rules: calendar edge cases, `BYSETPOS`, `WKST` | 36 |
| `sheet` | a spreadsheet evaluator to an invented spec: errors, laziness, cycles | 58 |
| `justify` | text justification with the familiar rules changed | 19 |
| `orderbook` | five bugs in an order-matching function, none of them obvious | 16 |

The first four are the easy tier: strong models score 100% on them, but they still separate weaker ones.

## Usage

1. For each model, task and run (1-5): open a **fresh chat**, paste `tasks/<task>.md`, and save the whole
   reply as `answers/<model>/<task>_<run>.md`.
   - Keep the model's normal sampling settings. At temperature 0 the 5 runs come out identical.
   - For coding agents and IDE assistants, see [below](#agents-and-ide-assistants).
2. `python3 score.py answers`, add `-v` to see which cases failed:

```
model                   bugfix          calc      duration        semver   overall
model-a               100% 5/5       94% 2/5      100% 5/5       85% 1/5       95%
```

A cell like `94% 2/5` means 94% of cases passed on average, and 2 of the 5 runs were fully correct.

`answers/` is git-ignored, so your results stay local.

## Agents and IDE assistants

Agents such as IBM Bob or OpenCode take the same tasks, with two extra rules:

- **Work in an empty folder, never in this repo.** Agents read their workspace, so here they would find the
  cases and the reference answers. An empty folder also keeps each call's context, and token cost, small.
- **Start a fresh session for every run**, so an agent never sees its earlier answer.

### In the IDE chat panel

1. Open an empty folder as the workspace.
2. Start a new chat, paste `tasks/<task>.md`, and send it.
3. Save the reply as `answers/<agent>/<task>_<run>.md`. If the agent wrote the code to a file instead, copy
   that file there, under any extension.

### From the command line

Both tools have a one-shot mode with a fresh session per call, so the runs can be scripted. `run.sh` sends
every task to an agent command, each call in its own empty temp folder:

```bash
./run.sh <name> <agent command...>   # the prompt is added as the last argument
```

```bash
./run.sh bob bob --hide-intermediary-output -p            # Bob Shell
./run.sh model-a opencode run -m myprovider/model-a       # OpenCode with one model

for m in model-a model-b model-c model-d; do              # OpenCode, one result row per model
  ./run.sh "$m" opencode run -m "myprovider/$m"
done

RUNS=3 ./run.sh bob bob --hide-intermediary-output -p     # fewer runs, to save tokens
python3 score.py answers
```

- **Bob Shell:** `-p` needs API-key authentication, and the license must be accepted once
  (`bob --accept-license -p "hi"`). Leave out `--yolo`: without it Bob can't write files, so the code comes
  back in the reply, which is what gets scored.
- **OpenCode:** `-m` takes a `provider/model` ID, and `opencode models` lists the ones you have configured.
  To test your own models, add their endpoint as a provider in OpenCode's config. Flags differ between
  versions, so check `opencode run --help`.
- An agent's system prompt adds tokens to every call, so expect more usage than in a plain chat. If the budget
  is tight, 3 runs per task still show the differences.

## Self-check

`python3 score.py reference` must show 100% everywhere.

Answers run as plain Python on your machine, each in its own process with a 60 s timeout and `eval`/`exec`
disabled. Only score replies you are willing to execute.

Scoring is deterministic: the same answers give the same numbers on every run and every machine. The hash
seed is fixed, and the timeout only stops endless loops. It needs Python 3.10 or newer. The last line of the
output names the Python version, because an answer may use a standard-library feature that older versions
lack; compare results scored with the same version.
