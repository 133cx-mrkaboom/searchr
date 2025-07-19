# Scrape.py
# 2025 133cx-MRKABOOM
# Part of the Searchr Project

import requests
from bs4 import BeautifulSoup
import os

print("Scrape.py running")

def scrape_urls():
    input_file = "data/to_scrape.txt"
    output_file = "data/urls.txt"

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    # Clear output file before writing
    open(output_file, 'w').close()

    # Read URLs to scrape
    with open(input_file, "r") as file:
        urls = [line.strip() for line in file if line.strip()]

    for url in urls:
        print(f"\nScraping: {url}")

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        with open(output_file, 'a') as out_file:
            for link in links:
                href = link.get('href')
                if href:
                    print(href)
                    out_file.write(href + '\n')


if __name__ == "__main__":
    scrape_urls()
