from .bot import bot
from .services import get_or_create_user
from . import keyboards
from .models import UserMessage

PROFILE_IMAGE = "https://static.tildacdn.com/tild3536-3237-4036-b363-376361613861/errre.png"

@bot.message_handler(commands=['start'])
def start_handler(message):
    user = get_or_create_user(message)

    text = f"""
👋 Salom {user.first_name or "do‘st"}!

🤖 Men sizni **Ahrorjon** bilan tanishtiruvchi botman. 

Bu yerda mening loyihalarimni ko'rishingiz, men bilan bog'lanishingiz yoki ijtimoiy tarmoqlarimni kuzatishingiz mumkin.

👇 Kerakli bo'limni tanlang:
"""

    bot.send_photo(
        message.chat.id,
        PROFILE_IMAGE,
        caption=text,
        parse_mode="Markdown",
        reply_markup=keyboards.main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "🌐 Ijtimoiy tarmoqlar")
def socials_handler(message):
    bot.send_message(
        message.chat.id,
        "🔗 Mening ijtimoiy tarmoqlarim:",
        reply_markup=keyboards.social_links()
    )

@bot.message_handler(func=lambda m: m.text == "👨‍💻 Men haqimda")
def about_handler(message):
    about_text = """
🚀 **Backend Developer**
🛠 Stack: Python, Django, DRF, PostgreSQL, Docker.
📍 Bukhara, Uzbekistan.

Men murakkab tizimlar va API'lar yaratish bilan shug'ullanaman.
"""
    bot.send_message(message.chat.id, about_text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "📩 Xabar qoldirish")
def feedback_start(message):
    msg = bot.send_message(message.chat.id, "Marhamat, menga yubormoqchi bo'lgan xabaringizni yozing. Men uni albatta o'qiyman! 👇")
    bot.register_next_step_handler(msg, feedback_save)

def feedback_save(message):
    try:
        UserMessage.objects.create(
            user_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.first_name,
            text=message.text
        )
        bot.send_message(message.chat.id, "✅ Xabaringiz yuborildi! Rahmat.\n\nMen tez orada siz bilan bog'lanaman!")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ Xatolik yuz berdi. Keyinroq qayta urinib ko'ring.")

@bot.message_handler(func=lambda m: m.text == "📂 Loyihalarim")
def projects_handler(message):
    text = """
📂 **Mening loyihalarim:**

1. 🌐 Axror Tech Platform  
   — Portfolio + Blog + SaaS

2. 🤖 Telegram Bots  
   — Webhook asosida ishlovchi botlar

3. 💳 Payment Service  
   — TSPay integratsiyasi

👇 Batafsil ko‘rish uchun saytga o‘ting:
"""
    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=keyboards.projects_inline()
    )

