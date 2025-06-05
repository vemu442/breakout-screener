import requests
from bs4 import BeautifulSoup

def get_fundamentals(stock_name):
    try:
        url = f"https://www.screener.in/company/{stock_name}/consolidated/"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        ratios = soup.select("ul[class='ranges'] li")

        data = {}
        for li in ratios:
            parts = li.get_text(strip=True).split(":")
            if len(parts) == 2:
                key, value = parts
                data[key.strip()] = value.strip()
        return data
    except Exception as e:
        print(f"Error fetching fundamentals for {stock_name}: {e}")
        return {}