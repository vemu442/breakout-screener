import requests
import pandas as pd

def get_breakout_stocks():
    url = "https://chartink.com/screener/process"
    scan = {
        "scan_clause": "( {cash} ( latest close > latest supertrend(7,3) ) and ( latest close > latest sma(50) ) and ( latest volume > 1.5 * sma(20, volume) ) )"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://chartink.com/"
    }

    try:
        response = requests.post(url, data=scan, headers=headers, timeout=10)
        data = response.json()
        if "data" in data:
            df = pd.DataFrame(data["data"])
            df = df.rename(columns={"n": "Stock", "c": "Price"})
            return df
        return pd.DataFrame()
    except Exception as e:
        print("Error fetching stocks:", e)
        return pd.DataFrame()
