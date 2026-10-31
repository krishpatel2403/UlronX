#!/usr/bin/env bash
# jarvis-wrapper.sh — symlinked to ~/.local/bin/jarvis.
# Activates the managed venv and execs the real jarvis CLI.

ULTRONX_HOME="${ULTRONX_HOME:-$HOME/.ULTRONX}"
VENV="$ULTRONX_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "jarvis: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://ultronx.github.io/ULTRONX/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/jarvis" "$@"
