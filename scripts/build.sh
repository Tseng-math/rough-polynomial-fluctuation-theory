#!/usr/bin/env bash
set -euo pipefail
paper_root="$(cd "$(dirname "$0")/.." && pwd -P)"
export PYTHONDONTWRITEBYTECODE=1
exec python3 "$paper_root/scripts/build.py" "$@"
