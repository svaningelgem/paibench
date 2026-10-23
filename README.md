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
| `kth` | the k-th number with digit rules, k up to 10^18: counting instead of listing | 24 |
| `ring` | a lamp ring after up to 10^18 steps: seeing the algebra behind the rule | 18 |
| `avoid` | strings avoiding forbidden words, length up to 10^18: automaton plus matrix power | 21 |
| `cipher` | a text encoding given only as examples: finding the rule | 20 |
| `regions` | a grid transformation given only as examples: finding the rule | 14 |
| `reveal` | fewest announced places that fix a race result, 2·10^5 runners | 22 |
| `stall` | when to open a stall with a cooldown, arrival times up to 10^18 | 22 |
| `peaks` | counting sequences by a three-term maximum, length up to 10^9 | 21 |
| `erase` | shortest palindromes reachable by deletions, 10^4 range queries | 22 |
| `conquer` | whether one town can capture a whole road network | 22 |
| `arrows` | the best subset of 2·10^4 vectors, without trying subsets | 22 |
| `halves` | counting cheapest coupon assignments, 5·10^4 items | 22 |
| `shifts` | the best schedule after each of 2·10^4 changes | 22 |
| `records` | fewest swaps to a feasible log, hidden combinatorial structure | 22 |

The tasks come in tiers. The first four are easy: strong models score 100%, but they still separate weaker
ones. `ranges` to `orderbook` add dense specs and edge cases. In `kth`, `ring` and `avoid` the small cases can
be brute-forced, but the large ones need the right algorithm. `cipher` and `regions` describe the task only
through examples, and the hidden cases check whether the model found the actual rule.

`reveal` to `records` are contest problems, retold with new stories and adapted from AtCoder Grand Contest
problems. Their small cases are checked against brute force, so a correct but slow solution still gets those.
The large cases need the intended algorithm, and a slow one fails them by a wide margin.

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

Both tools have a one-shot mode with a fresh session per call, so the runs can be scripted. `bench.sh` runs the
contest tier 3 times through either tool and prints the scores:

```bash
./bench.sh bob                                            # Bob Shell
./bench.sh opencode myprovider/model-a myprovider/model-b # OpenCode, one result row per model
RUNS=5 TASKS=all ./bench.sh bob                           # every task, 5 runs
TASKS="calc ring" ./bench.sh bob                          # only these tasks
```

For other agents, `run.sh` sends every task (or the ones in `TASKS`) to any agent command, each call in its own
empty temp folder:

```bash
./run.sh <name> <agent command...>   # the prompt is added as the last argument
RUNS=3 ./run.sh bob bob --hide-intermediary-output -p     # what bench.sh does for Bob, on every task
python3 score.py answers             # TASKS limits the table to those tasks here too
```

- **Bob Shell:** `-p` needs API-key authentication, and the license must be accepted once
  (`bob --accept-license -p "hi"`). Leave out `--yolo`: without it Bob can't write files, so the code comes
  back in the reply, which is what gets scored.
- **OpenCode:** `-m` takes a `provider/model` ID, and `opencode models` lists the ones you have configured.
  To test your own models, add their endpoint as a provider in OpenCode's config. Flags differ between
  versions, so check `opencode run --help`.
- An agent's system prompt adds tokens to every call, so expect more usage than in a plain chat. If the budget
  is tight, 3 runs per task still show the differences.
- If you switch an agent's tools off, replace its system prompt with a plain one as well. A prompt that
  promises tools can make the model write out fake tool calls instead of the code.

## Self-check

`python3 score.py reference` must show 100% everywhere.

Answers run as plain Python on your machine, each in its own process with `eval`/`exec` disabled. Only
score replies you are willing to execute. Each case gets 10 s; a case that hangs or crashes fails on its own,
and the remaining cases still run.

Scoring is deterministic: the same answers give the same numbers on every run and every machine. The hash
seed is fixed. The large cases are sized so that a right solution needs at most a second or two (the
reference, in plain Python) and brute force would need far longer than 10 s, so a faster or slower machine
doesn't change the result. Scoring needs Python 3.10 or newer. The last line of the output names the Python
version, because an answer may use a standard-library feature that older versions lack; compare results
scored with the same version.
