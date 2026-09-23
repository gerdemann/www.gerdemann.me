#!/usr/bin/env python3
"""Stop only the Hugo process started by this checkout's preview script."""
import os
import signal
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
pid_file = root / '.preview.pid'
if not pid_file.exists():
    raise SystemExit('Keine gespeicherte Vorschau gefunden.')
pid = int(pid_file.read_text().strip())
command = subprocess.run(['ps', '-p', str(pid), '-o', 'command='], capture_output=True, text=True).stdout
if 'hugo server --config config.toml,preview.toml --bind 127.0.0.1' not in command:
    raise SystemExit('Der gespeicherte Prozess ist keine passende Vorschau. Kein Prozess wurde beendet.')
os.kill(pid, signal.SIGTERM)
pid_file.unlink(missing_ok=True)
(root / '.preview.port').unlink(missing_ok=True)
print('Lokale Vorschau beendet.')
