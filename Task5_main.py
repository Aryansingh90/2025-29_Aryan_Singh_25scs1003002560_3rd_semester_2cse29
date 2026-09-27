import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
OUTPUT_FILE = "products.csv"


def scrape_books(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    for book in soup.select("article.product_pod"):
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one(".price_color")
        rating_tag = book.select_one("p.star-rating")

        title = title_tag.get("title", "Unknown") if title_tag else "Unknown"
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        rating = "Unknown"
        if rating_tag:
            classes = rating_tag.get("class", [])
            rating_names = {"One": "1", "Two": "2", "Three": "3",
                            "Four": "4", "Five": "5"}
            for name, value in rating_names.items():
                if name in classes:
                    rating = value
                    break

        products.append({
            "name": title,
            "price": price,
            "rating": rating
        })

    return products


def save_to_csv(products, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "rating"])
        writer.writeheader()
        writer.writerows(products)


def main():
    try:
        products = scrape_books(URL)
        save_to_csv(products, OUTPUT_FILE)
        print(f"Scraped {len(products)} products.")
        print(f"Data saved to {OUTPUT_FILE}")
    except requests.RequestException as error:
        print(f"Could not access the website: {error}")
    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
