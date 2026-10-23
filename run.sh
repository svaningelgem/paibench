#!/usr/bin/env bash
# Run every task through a one-shot CLI agent, each call in a fresh empty folder.
# Usage: [RUNS=5] [TASKS="calc ring"] ./run.sh <name> <agent command...>   (the prompt is appended as the last argument)
set -euo pipefail

name=$1
shift
repo=$(cd "$(dirname "$0")" && pwd)
for task in ${TASKS:-}; do
  [[ -f "$repo/tasks/$task.md" ]] || { echo "unknown task: $task" >&2; exit 2; }
done
mkdir -p "$repo/answers/$name"
for run in $(seq "${RUNS:-5}"); do
  for task in ${TASKS:-$(cd "$repo/tasks" && ls -- *.md | sed 's/\.md$//')}; do
    out="$repo/answers/$name/${task}_$run.md"
    echo "$name: $task run $run" >&2
    dir=$(mktemp -d)
    (cd "$dir" && "$@" "$(cat "$repo/tasks/$task.md")") > "$out" || echo "failed: $out" >&2
    rm -rf "$dir"
  done
done
