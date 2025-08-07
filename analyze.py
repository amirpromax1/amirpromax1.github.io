
import openai
import os

# گرفتن کلید API از متغیر محیطی
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

# تحلیلگر بازار کریپتو
def analyze_market():
    prompt = """
    اول اطلاعاتت رو با استفاده از اینترنت بروز کن سپس لطفاً تحلیل کاملی از بازار کریپتو ارائه بده که شامل این موارد باشه:
    1. روند کلی مارکت
    2. تحلیل روند ۱۰ ارز دیجیتال برتر
    3. نقاط حمایت و مقاومت برای هرکدوم
    4. پیش‌بینی برای هر ارز در تایم‌فریم ۴ ساعته
    5. پیشنهاد یک ترید مناسب برای هر ارز با ذکر دلیل

     فقط تحلیل دقیق و حرفه‌ای بده، از نوشتن چیزای عمومی و بی‌استفاده خودداری کنو پیام بعدیت شامل چیزایی که گفتم باشه وقبل اریه اینا چیز دیگری ننویسطفاً بدون مقدمه‌چینی یا جملات عمومی مثل 'متوجه شدم' یا 'در حال به‌روزرسانی اطلاعات'، فقط پاسخ دقیق، فنی، و کاربردی بده. از توضیحات غیرضروری خودداری کن..
    """

    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک تحلیل‌گر حرفه‌ای بازار کریپتو هستی."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response['choices'][0]['message']['content']

    with open("analysis.txt", "w", encoding="utf-8") as file:
        file.write(result)

# اجرای تحلیل
if __name__ == "__main__":
    analyze_market()
