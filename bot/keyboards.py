from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📂 Loyihalarim", "👨‍💻 Men haqimda")
    markup.row("📩 Xabar qoldirish")
    markup.row("🌐 Ijtimoiy tarmoqlar",)
    return markup


def back_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("⬅️ Orqaga")
    return markup

def social_links():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("GitHub", url="https://github.com/axrorback"))
    markup.add(types.InlineKeyboardButton("LinkedIn", url="https://linkedin.com/in/axrorback"))
    markup.add(types.InlineKeyboardButton("Telegram", url="https://t.me/axrorback"))
    markup.add(types.InlineKeyboardButton("Instagram", url="https://instagram.com/axrorback"))
    markup.add(types.InlineKeyboardButton("Twitter", url="https://twitter.com/axrorback"))
    markup.add(types.InlineKeyboardButton("Facebook", url="https://facebook.com/axrorback"))
    markup.add(types.InlineKeyboardButton("Web-site", url="https://www.axror.tech"))
    return markup

def projects_inline():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🌐 Web-site", url="https://www.axror.tech"))
    markup.add(types.InlineKeyboardButton("💻 GitHub", url="https://github.com/axrorback"))
    return markup
