import requests
import os

def analyze_market():
    api_key = os.getenv("OPENROUTER_API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    message = """
با توجه به داده‌های لحظه‌ای قیمت ارزهای دیجیتال زیر، یک تحلیل کامل بده.
- روند کلی مارکت
- تحلیل روند هر کدوم از ۱۰ ارز برتر
- نقاط حمایت و مقاومت هرکدام
- پیش‌بینی تایم فریم ۴ ساعته
- پیشنهاد ترید هوش مصنوعی برای هرکدام
پاسخ رو کامل، دقیق و منظم بده.
"""

    data = {
        "model": "openrouter/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        output = result["choices"][0]["message"]["content"]

        with open("analysis.txt", "w", encoding="utf-8") as f:
            f.write(output)

        print("✅ تحلیل ذخیره شد.")
    except Exception as e:
        print("❌ خطا در دریافت پاسخ:")
        print(response.text)
        raise e

if __name__ == "__main__":
    analyze_market()
