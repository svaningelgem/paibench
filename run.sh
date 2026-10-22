#!/usr/bin/env bash
# Run every task through a one-shot CLI agent, each call in a fresh empty folder.
# Usage: [RUNS=5] ./run.sh <name> <agent command...>   (the prompt is appended as the last argument)
set -euo pipefail

name=$1
shift
repo=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$repo/answers/$name"
for run in $(seq "${RUNS:-5}"); do
  for task in "$repo"/tasks/*.md; do
    out="$repo/answers/$name/$(basename "$task" .md)_$run.md"
    echo "$name: $(basename "$task" .md) run $run" >&2
    dir=$(mktemp -d)
    (cd "$dir" && "$@" "$(cat "$task")") > "$out" || echo "failed: $out" >&2
    rm -rf "$dir"
  done
done
