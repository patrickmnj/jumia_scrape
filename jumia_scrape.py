import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.jumia.co.ke/"

response = requests.get(url)
# rate_url = "https://api.frankfurter.dev/v2/rate/KES/USD"



print("statuscode:", response .status_code)

soup = BeautifulSoup(response.text, "html.parser")

rate_url = "https://api.frankfurter.dev/v2/rate/KES/USD"

rate_response = requests.get(rate_url)

print("Currency API status:", rate_response.status_code)

rate_data = rate_response.json()

rate = rate_data["rate"]

print("KES to USD rate:", rate)

items= soup.select("article.prd")
print("items found:", len(items))

scraped_items = []

for item in items[:100]:

    name = item.select_one(".name")
    price = item.select_one(".prc")

    if not name or not price:
        continue

    item_name = name.get_text(strip=True)
    price_text = price.get_text(strip=True)

    if not item_name or not price_text:
        continue

    price_kes = float(
        price_text.replace("KSh", "").replace(",", "").strip()
    )

    price_usd = price_kes * rate
    
    scraped_items.append({
    "item name": item_name,
    "price(KES)": price_kes,
    "price(USD)": round(price_usd, 2)
})
    if len(scraped_items) ==100:
        break
    print("item:", item_name)
    print("price:", price_text)
    print("USD:", round(price_usd, 2))
    print("-" * 50)
    
df =pd.DataFrame(scraped_items)

print("\nscraped items")

print(df.to_string(index=False))

df.to_csv("jumia_items.csv", index=False)
print("saved",len(df), "items to jumia_items.csv")
