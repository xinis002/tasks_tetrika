import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict
import time

BASE_URL = "https://ru.wikipedia.org"
START_PATH = "/w/index.php?title=Категория:Животные_по_алфавиту"
OUTPUT_CSV = "beasts.csv"

def get_page(url):
    full_url = BASE_URL + url
    response = requests.get(full_url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")

def parse_all_pages():
    url = START_PATH
    counts = defaultdict(int)
    page_number = 1

    while url:
        print(f"[{page_number}] Обрабатываем страницу: {url}")
        page_number += 1
        soup = get_page(url)

        for group in soup.select("div.mw-category-group"):
            for item in group.find_all("li"):
                name = item.get_text(strip=True)
                if name:
                    first_letter = name[0].upper()


                    if 'А' <= first_letter <= 'Я' or first_letter == "Ё":
                        if first_letter == 'Ё':
                            first_letter = 'Е'

                        counts[first_letter] += 1


        next_link = soup.find("a", string="Следующая страница")
        if next_link and next_link.has_attr("href"):
            url = next_link["href"]
            time.sleep(0.5)
        else:
            break

    return counts

def save_to_csv(counts):
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])

if __name__ == "__main__":
    results = parse_all_pages()
    save_to_csv(results)
    print("\n Готово! Данные записаны в beasts.csv")

