import os
import requests
from openai import OpenAI

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
    summary = "قیمت لحظه‌ای ارزهای دیجیتال":
"
    for coin, price in prices.items():
        summary += f"- {coin.title()}: ${price['usd']}
"

    prompt = summary + "\nبا توجه به قیمت‌ها، تحلیل کامل شامل:\n- روند کلی بازار\n- تحلیل هر ارز\n- حمایت/مقاومت\n- پیش‌بینی تایم ۴ ساعته\n- پیشنهاد ترید"

    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    response = client.chat.completions.create(
        model="openrouter/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای ارز دیجیتال هستی."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content
    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    analyze_market()
