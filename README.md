# Multi-Category Book Scraper

A Python pipeline that scrapes every book (title, price, rating) from four 
categories on [books.toscrape.com](https://books.toscrape.com), a site made for 
practising scraping. It follows each category's pages to the end, merges 
everything into one CSV, and charts the average price and rating per category.

---

## Features

- Scrapes title, price, and rating from multiple categories, following pagination so every book in a category is collected (not just the first 20)
- Polite, fault-tolerant requests — timeouts, HTTP error checks, a short delay between pages, and a failed category is skipped instead of crashing the run
- Cleans and structures scraped datasets using pandas
- Merges datasets into one unified CSV
- Calculates average category statistics
- Generates 2 comparison charts saved as PNG files

---

### Categories Used

- Mystery
- Classics
- Thriller
- Philosophy

---

## Project Structure

```
Multi-Category-Book-Scraper/
│
├── scraper/
│   ├── __init__.py
│   └── books.py            # scrapes every page of a category
│
├── processors/
│   ├── __init__.py
│   ├── cleaner.py          # cleans price and rating columns
│   └── merger.py           # merges multiple dataframes into one
│
├── visualizer/
│   ├── __init__.py
│   └── charts.py           # generates bar charts from merged data
│
├── data/
│   └── combined_books.csv    # full scraped dataset for reference
│
├── screenshots/             # chart previews for README
│   ├── avg_price.png
│   └── avg_rating.png
│
├── main.py                # pipeline entry point
├── output/                # generated at runtime (gitignored)
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the pipeline
```bash
python main.py
```

---

## Output

Running the pipeline generates the following files in `output/`:
- `combined_books.csv` — full merged dataset (also saved to `data/` for reference)
- `avg_price.png` — average price comparison chart
- `avg_rating.png` — average rating comparison chart

> `output/` is excluded from the repository. Run the script to generate these files locally.

---

## Visualizations

**Average Price by Category**

![Average Price](screenshots/avg_price.png)

**Average Rating by Category**

![Average Rating](screenshots/avg_rating.png)

---

## Tech Stack

- Python
- lxml
- requests
- BeautifulSoup4
- pandas
- matplotlib

---

## Author

Manish Pandeya
