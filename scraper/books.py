import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MultiCategoryBookScraper/1.0)"}
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def fetch_page(session, url):
    """Download one page and return it parsed. Raises on network errors
    or a bad HTTP status, so the caller can decide what to do."""
    response = session.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()  # turns a 404/500 into an error instead of parsing an error page
    return BeautifulSoup(response.content, "lxml")  # .content lets BeautifulSoup handle decoding — avoids encoding issues with £ symbols


def scrape_books(url, session=None, delay=0.5):
    """Scrape every page of one category, following the 'next' link until
    there isn't one. delay: seconds to wait between pages, to be polite."""
    session = session or requests.Session()  # a Session reuses the connection across pages
    data = []
    category = None
    page_url = url

    while page_url:
        soup = fetch_page(session, page_url)

        if category is None:
            category = soup.find("h1").text.strip()

        for book in soup.find_all("article", class_="product_pod"):
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            raw_rating = book.find("p", class_="star-rating")["class"][1]

            data.append({
                "Title": title,
                "Price": price,
                "Rating": RATING_MAP.get(raw_rating),
                "Category": category,
            })

        # Categories with more than 20 books are split across pages.
        # The "next" link is relative (e.g. "page-2.html"), so urljoin
        # turns it into a full URL based on the current page.
        next_link = soup.select_one("li.next a")
        page_url = urljoin(page_url, next_link["href"]) if next_link else None
        if page_url:
            time.sleep(delay)

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = scrape_books("https://books.toscrape.com/catalogue/category/books/classics_6/index.html")
    print(df)
