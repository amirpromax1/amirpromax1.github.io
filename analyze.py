import openai
import requests
import os

def fetch_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,tether,binancecoin,solana,cardano,dogecoin,tron,polkadot,polygon,chainlink',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    return response.json()

def analyze_market():
    prices = fetch_prices()
    summary = "قیمت لحظه‌ای ۱۰ ارز برتر دیجیتال:\n"
    for coin, price in prices.items():
        summary += f"- {coin.title()}: ${price['usd']}\n"

    message = summary + "\nبا توجه به قیمت‌های بالا، یک تحلیل کامل انجام بده که شامل روند کلی مارکت، تحلیل تکنیکال هر ارز، نقاط حمایت و مقاومت، پیش‌بینی تایم‌فریم ۴ ساعته، و یک پیشنهاد ترید برای هرکدام باشه."

    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    openai.api_base = "https://openrouter.ai/api/v1"

    result = openai.ChatCompletion.create(
        model="openrouter/mistral-7b-instruct",
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای ارز دیجیتال هستی."},
            {"role": "user", "content": message}
        ]
    )

    output = result["choices"][0]["message"]["content"]
    with open("analysis.txt", "w", encoding="utf-8") as file:
        file.write(output)

if __name__ == "__main__":
    analyze_market()