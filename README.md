# Playwright to Markdown
This script visits a webpage (like a browser would), grabs the HTML content, and converts it into Markdown — a simpler text format used in README files and notes.

Environment is Astral UV for Python Project and Package Management.

Thank you to the creators of Markdownify, Playwright and ArgParse for the use of their packages/modules.

## Setup Instructions

```sh
git clone this repo
uv sync
source .venv/bin/activate
playwright install
```

## Run Instructions

```sh
uv run main.py --url https://www.example.com --tofile output.md
```
