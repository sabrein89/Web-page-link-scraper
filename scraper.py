import requests
from bs4 import BeautifulSoup
import csv

url = "Insert the target URL here"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("[*] Sending HTTP request...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("[*] Page loaded. Parsing content...")
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links inside the relevant table
    table_links = soup.select("table a")
    data = [(link.text.strip(), link.get("href")) for link in table_links if link.get("href")]

    print(f"[*] Found {len(data)} entries. Saving to CSV...")
    with open("bdgov_links.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "URL"])
        writer.writerows(data)

    print("[✅] Done! File saved as scraped_links.csv")
else:
    print(f"[!] Failed to load page. Status code: {response.status_code}")
