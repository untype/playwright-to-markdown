# This script visits a webpage (like a browser would), grabs the HTML content,
# and converts it into Markdown — a simpler text format used in README files and notes.
# Run it from the command line with: python main.py --url https://example.com
# Optionally save the output to a file with: --tofile output.md
# Thank you to Markdownify, Playwright and ArgParse for the use of their packages/modules.

import markdownify
from playwright.sync_api import sync_playwright
import argparse

def main():

    # Set up the command-line argument parser so users can pass in options when running the script
    parser = argparse.ArgumentParser(description='Scrape a webpage and convert it to Markdown format.')

    # Add the --url option so the user can specify which webpage to scrape
    parser.add_argument('--url', type=str, help='The URL of the webpage to scrape')

    # Add the optional --tofile option; if provided, the output is saved to that file instead of printed
    parser.add_argument('--tofile', type=str, help='The output file to save the Markdown content')

    # Read the arguments the user passed in from the command line
    args = parser.parse_args()

    # This function opens a headless browser (invisible), loads the page, grabs the HTML,
    # then converts it to Markdown using the markdownify library
    def scrape_and_transform_to_markdown(url):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            content = page.content()
            browser.close()
            md_content = markdownify.markdownify(content)
        return md_content

    # Check if the user wants to save the output to a file or just print it to the terminal
    if args.tofile:
        markdown_content = scrape_and_transform_to_markdown(args.url)
        with open(args.tofile, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        print(f'Markdown content saved to {args.tofile}')
    else:
        markdown_content = scrape_and_transform_to_markdown(args.url)
        print(markdown_content)

if __name__ == "__main__":
    main()
