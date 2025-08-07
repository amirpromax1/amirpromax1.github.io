import requests
import os

# گرفتن قیمت ارزها از CoinGecko
def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

# فرستادن به OpenRouter (Claude 3 Haiku رایگان)
def analyze(prices, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = (
        f"تحلیل قیمت‌ها:\n"
        f"- بیت‌کوین: {prices['bitcoin']['usd']} دلار\n"
        f"- اتریوم: {prices['ethereum']['usd']} دلار\n"
        f"- بایننس‌کوین: {prices['binancecoin']['usd']} دلار\n"
        f"آیا بازار صعودیه یا نزولی؟ خیلی ساده و کوتاه تحلیل کن."
    )

    data = {
        "model": "anthropic/claude-3-haiku:beta",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

def main():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    prices = get_prices()
    result = analyze(prices, api_key)

    with open("analysis_btc.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("✅ تحلیل ذخیره شد.")

if __name__ == "__main__":
    main()