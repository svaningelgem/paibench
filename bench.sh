#!/usr/bin/env bash
# Run the benchmark through Bob Shell or OpenCode, then print the scores.
# Usage: ./bench.sh bob
#        ./bench.sh opencode <provider/model> [<provider/model> ...]
# RUNS sets the runs per task (default 3). TASKS picks the tasks: the contest tier by default, "all" for every task.
set -euo pipefail
cd "$(dirname "$0")"

export RUNS=${RUNS:-3}
export TASKS=${TASKS:-reveal stall peaks erase conquer arrows halves shifts records}
[[ $TASKS == all ]] && unset TASKS

case ${1:-} in
  bob)
    ./run.sh bob bob --hide-intermediary-output -p
    ;;
  opencode)
    shift
    (($#)) || { echo "name at least one provider/model" >&2; exit 2; }
    for model in "$@"; do
      ./run.sh "${model##*/}" opencode run -m "$model"
    done
    ;;
  *)
    sed -n '2,5p' "$0" >&2
    exit 2
    ;;
esac
python3 score.py answers
