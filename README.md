# VoiceApp (Native Desktop App)

This repository is set up as a **native desktop app project**, not an HTML/web page.

## What this gives you

- A local desktop application built with Python + Tkinter (native GUI toolkit)
- No HTML frontend required
- GitHub Actions workflow that builds distributable app binaries for:
  - Linux
  - Windows
  - macOS

## Run locally

```bash
python3 app/main.py
```

## Build locally (single-file app)

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --name voiceapp app/main.py
```

The binary will be created in `dist/`.

## GitHub build artifacts

Every push to `main` (and manual workflow runs) will produce app artifacts in the Actions tab.
Download the artifact for your OS and run it like a normal app.
