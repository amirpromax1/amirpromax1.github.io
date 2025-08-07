
import openai
import os

def analyze_market():
    openai.api_base = "https://openrouter.ai/api/v1"
    openai.api_key = os.getenv("OPENROUTER_API_KEY")

    prompt = """
شما یک تحلیل‌گر حرفه‌ای بازار ارز دیجیتال هستید. لطفاً یک تحلیل کامل برای امروز بنویسید که شامل موارد زیر باشد:

۱. تحلیل روند کلی بازار ارز دیجیتال (مثلاً بازار در حالت صعودی، نزولی یا در حال نوسان است)

۲. بررسی دقیق ۱۰ ارز دیجیتال برتر زیر:
BTC, ETH, BNB, XRP, SOL, ADA, DOGE, AVAX, DOT, LINK

برای هر ارز موارد زیر را تحلیل کنید:
- روند فعلی (صعودی / نزولی / خنثی)
- نقاط حمایت و مقاومت کلیدی
- پیش‌بینی در تایم‌فریم ۴ ساعته
- پیشنهاد ترید (مثلاً خرید، فروش یا تماشاگر بودن) و دلیل منطقی برای این پیشنهاد از نگاه شما

لحن تحلیل رسمی، فارسی و قابل فهم برای معامله‌گران باشد.
خروجی را به‌صورت واضح و قابل خواندن برای نمایش در وب‌سایت ارائه بده.
    """

    response = openai.ChatCompletion.create(
        model="openchat/openchat-3.5-1210",
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای بازار کریپتو هستید."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content.strip()

    with open("analysis_btc.txt", "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    analyze_market()
