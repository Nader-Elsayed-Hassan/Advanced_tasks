import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.jumia.com.eg/catalog/?q=phone"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="prd")

data = []

for item in products:
    name = item.find("h3", class_="name")
    price = item.find("div", class_="prc")
    link_tag = item.find("a", href=True)

    data.append({
        "Name": name.text.strip() if name else "N/A",
        "Price": price.text.strip() if price else "N/A",
        "Link": "https://www.jumia.com.eg" + link_tag["href"] if link_tag else "N/A"
    })

df = pd.DataFrame(data)

df.to_excel("jumia_products.xlsx", index=False)

print("Saved successfully → jumia_products.xlsx")
