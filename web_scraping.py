
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Website to scrape
url = "https://books.toscrape.com/"

# Get webpage content
response = requests.get(url, timeout=20)
response.raise_for_status()

# Read HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store book information
books_data = []

# Find all books on the page
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text(strip=True)

    books_data.append({
        "Book Title": title,
        "Price": price
    })

# Convert data into a table
df = pd.DataFrame(books_data)

# Save as a CSV file
df.to_csv("scraped_books.csv", index=False)

print("Total books collected:", len(df))
print("Data saved successfully to scraped_books.csv")
print("\nFirst five records:")
print(df.head())

