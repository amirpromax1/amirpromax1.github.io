import requests
import json
import os

def analyze_market():
    api_key = os.getenv("OPENROUTER_API_KEY")

    message = "با توجه به داده‌های لحظه‌ای قیمت ارزهای دیجیتال زیر، یک تحلیل کامل بده:"
    coins = ["bitcoin", "ethereum", "bnb", "solana", "xrp", "cardano", "dogecoin", "avalanche", "toncoin", "shiba-inu"]
    summary = ""

    for coin in coins:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        price = response.json().get(coin, {}).get('usd', 'نامشخص')
        summary += f"{coin.title()}: ${price}\n"

    full_prompt = f"""{message}
{summary}
تحلیل بازار را در تایم فریم ۴ ساعته بنویس و در پایان یک پیشنهاد ترید بده."""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": full_prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    result = response.json()
    output = result["choices"][0]["message"]["content"]

    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(output)

analyze_market()
