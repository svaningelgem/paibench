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

Both tools have a one-shot mode with a fresh session per call, so all 20 runs can be scripted. Run this from
the repo root, with the `agent` line for your tool:

```bash
agent() { bob --hide-intermediary-output -p "$1"; }      # Bob Shell
# agent() { opencode run -m <provider>/<model> "$1"; }   # OpenCode
name=bob

repo=$PWD
mkdir -p "answers/$name"
for run in 1 2 3 4 5; do
  for task in duration bugfix calc semver; do
    (cd "$(mktemp -d)" && agent "$(cat "$repo/tasks/$task.md")") > "answers/$name/${task}_$run.md"
  done
done
python3 score.py answers
```

- **Bob Shell:** `-p` needs API-key authentication, and the license must be accepted once
  (`bob --accept-license -p "hi"`). Leave out `--yolo`: without it Bob can't write files, so the code comes
  back in the reply, which is what gets scored.
- **OpenCode:** `-m` can point at your own models too, so you can score plain models and agents on the same
  footing. Check `opencode run --help`, because the flags differ between versions.
- An agent's system prompt adds tokens to every call, so expect more usage than in a plain chat. If the budget
  is tight, 3 runs per task still show the differences.

## Self-check

`python3 score.py reference` must show 100% everywhere.

Answers run as plain Python on your machine, each in its own process with a 10 s timeout and `eval`/`exec`
disabled. Only score replies you are willing to execute.
