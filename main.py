import os

import requests

from processors import clean_data, merge_datasets
from scraper import scrape_books
from visualizer import generate_charts

BASE = "https://books.toscrape.com/catalogue/category/books"

# Add or remove categories here — the rest of the pipeline adapts.
CATEGORIES = {
    "Mystery": f"{BASE}/mystery_3/index.html",
    "Classics": f"{BASE}/classics_6/index.html",
    "Thriller": f"{BASE}/thriller_37/index.html",
    "Philosophy": f"{BASE}/philosophy_7/index.html",
}


def main():
    session = requests.Session()
    cleaned = []

    for name, url in CATEGORIES.items():
        try:
            raw = scrape_books(url, session=session)
        except requests.RequestException as e:
            # One broken category shouldn't throw away the others.
            print(f"Skipping {name}: {e}")
            continue
        print(f"{name}: {len(raw)} books")
        cleaned.append(clean_data(raw))

    if not cleaned:
        print("No categories could be scraped — check your internet connection.")
        return

    combined_df = merge_datasets(*cleaned)

    generate_charts(combined_df)

    os.makedirs("output", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    combined_df.to_csv("output/combined_books.csv", index=False)
    combined_df.to_csv("data/combined_books.csv", index=False)  # reference copy kept in the repo

    print(
        f"Scraped {len(combined_df)} books across {combined_df['Category'].nunique()} categories "
        f"→ saved to output/combined_books.csv and data/combined_books.csv"
    )


if __name__ == "__main__":
    main()
