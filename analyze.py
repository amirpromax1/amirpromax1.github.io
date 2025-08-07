import openai
import os

def analyze_market():
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    openai.api_base = "https://openrouter.ai/api/v1"  # ✅ مهم

    prompt = (
        "1. روند کلی مارکت کریپتو رو تحلیل کن\n"
        "2. روند هر کدوم از ۱۰ ارز دیجیتال برتر رو بررسی کن\n"
        "3. نقاط حمایت و مقاومت هر کدوم رو بگو\n"
        "4. پیش‌بینی در تایم‌فریم ۴ ساعته برای هر ارز ارائه بده\n"
        "5. یک پیشنهاد ترید هوشمندانه برای هر ارز بده که بشه ازش سود گرفت"
    )

    response = openai.ChatCompletion.create(
        model="openrouter/gpt-3.5-turbo",  # ✅ برای OpenRouter این فرمت درسته
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای بازار کریپتو هستی."},
            {"role": "user", "content": prompt}
        ]
    )

    analysis = response.choices[0].message.content

    with open("analysis_btc.txt", "w", encoding="utf-8") as f:
        f.write(analysis)

if __name__ == "__main__":
    analyze_market()
