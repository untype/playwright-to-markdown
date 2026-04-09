Playwright to Markdown
======================

This script visits a webpage (like a browser would), grabs the HTML content, and converts it into Markdown — a simpler text format used in README files and notes.

Thank you to the creators of Markdownify, Playwright and ArgParse for the use of their packages/modules.

Setup Instructions
==================
git clone this repo
uv sync
.venv/Scripts/activate
playwright install

Run Instructions
================
uv run main.py --url https://www.example.com --tofile output.md
