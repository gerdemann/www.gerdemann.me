#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
command -v hugo >/dev/null || { echo 'Hugo fehlt. Installation: brew install hugo'; exit 1; }
port=$(python3 - <<'PYPORT'
import socket
for port in range(1313, 1350):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try: s.bind(('127.0.0.1', port))
        except OSError: continue
        print(port)
        break
else: raise SystemExit('Kein freier Port zwischen 1313 und 1349.')
PYPORT
)
printf '\nLokale Vorschau: http://127.0.0.1:%s/\nBeenden: Ctrl+C\n\n' "$port"
printf '%s\n' "$$" > .preview.pid
printf '%s\n' "$port" > .preview.port
exec hugo server --config config.toml,preview.toml --bind 127.0.0.1 --port "$port" --baseURL "http://127.0.0.1:$port/" --disableFastRender --noHTTPCache
