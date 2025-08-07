import openai
import requests

def get_prices():
    coins = ["bitcoin", "ethereum", "bnb", "ripple", "solana", "cardano", "dogecoin", "avalanche", "tron", "polkadot"]
    ids = "%2C".join(coins)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

def format_price_summary(prices):
    summary = ""
    for coin, price in prices.items():
        summary += f"{coin.title()}: ${price['usd']}
"
    return summary

def analyze_market():
    prices = get_prices()
    price_summary = format_price_summary(prices)

    message = f"""با توجه به داده‌های قیمت لحظه‌ای ارزهای دیجیتال زیر، یک تحلیل کامل بده:
{price_summary}"""

    response = openai.ChatCompletion.create(
        model="openrouter/mistralai/mistral-7b-instruct",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای بازار رمزارز هستید."},
            {"role": "user", "content": message}
        ]
    )

    analysis = response.choices[0].message.content

    with open("analysis.txt", "w", encoding="utf-8") as file:
        file.write(analysis)

if __name__ == "__main__":
    analyze_market()
