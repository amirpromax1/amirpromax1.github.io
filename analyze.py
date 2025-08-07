import openai
import requests
import os

def get_market_prices():
    coins = [
        "bitcoin", "ethereum", "binancecoin", "solana",
        "ripple", "cardano", "dogecoin", "avalanche-2",
        "polkadot", "tron"
    ]
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd"
    try:
        res = requests.get(url)
        res.raise_for_status()
        prices = res.json()
        return prices
    except Exception as e:
        return {}

def create_prompt(prices):
    message = "با توجه به داده‌های قیمت لحظه‌ای ارزهای دیجیتال زیر، یک تحلیل کامل بده:
"
    for coin, data in prices.items():
        usd = data.get("usd", "نامشخص")
        message += f"- {coin.title()}: ${usd}
"
    message += "\nتحلیل شامل موارد زیر باشد:\n"
    message += "- روند کلی بازار\n"
    message += "- روند هر ارز\n"
    message += "- نقاط حمایت و مقاومت هر کدام\n"
    message += "- پیش‌بینی در تایم‌فریم ۴ ساعته\n"
    message += "- یک پیشنهاد ترید برای هرکدام\n"
    return message

def analyze_market():
    prices = get_market_prices()
    prompt = create_prompt(prices)

    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    openai.api_base = "https://openrouter.ai/api/v1"

    response = openai.ChatCompletion.create(
        model="openrouter/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای ارز دیجیتال هستید."},
            {"role": "user", "content": prompt}
        ]
    )

    analysis = response["choices"][0]["message"]["content"]

    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(analysis)

if __name__ == "__main__":
    analyze_market()