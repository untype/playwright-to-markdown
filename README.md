** playwright-to-markdown **

This script visits a webpage (like a browser would), grabs the HTML content,
nd converts it into Markdown — a simpler text format used in README files and notes.

Run it from the command line with: python main.py --url https://example.com

Optionally save the output to a file with: --tofile output.md

Thank you to Markdownify, Playwright and ArgParse for the use of their packages/modules.

Setup Instructions
====================
uv sync
.venv/Scripts/activate
playwright install

Run Instructions
====================
uv run main.py --url https://www.example.com --tofile output.md
