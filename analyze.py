
import os
import requests
import google.generativeai as genai

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

    summary = "📊 قیمت لحظه‌ای ارزهای دیجیتال:\n"
    for coin, price in prices.items():
        summary += f"- {coin.title()}: ${price['usd']}\n"

    prompt = summary + "\nبا توجه به قیمت‌ها، تحلیل کامل شامل:\n- روند کلی بازار\n- تحلیل هر ارز\n- حمایت/مقاومت\n- پیش‌بینی تایم ۴ ساعته\n- پیشنهاد ترید برای هرکدام\nهمه چیز رو به زبان فارسی بنویس."

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    output = response.text
    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    analyze_market()
