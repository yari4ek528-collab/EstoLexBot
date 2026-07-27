from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8847485249:AAFwZvPW9fOwenoUpLfVZKn5XP8UTuwOqCk"

dictionary = {
    "привет": "tere",
    "спасибо": "aitäh",
    "да": "jah",
    "нет": "ei",
    "дом": "maja",
    "кот": "kass",
    "собака": "koer",
    "машина": "auto",
    "вода": "vesi",
    "хлеб": "leib",
}

main_keyboard = ReplyKeyboardMarkup(
    [
        ["📖 Перевести", "🔍 Поиск"],
        ["📚 Учить слова", "⭐ Избранное"],
        ["➕ Добавить слово", "📊 Статистика"],
        ["⚙️ Настройки", "ℹ️ Помощь"],
    ],
    resize_keyboard=True,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в EstoLex!\n\n"
        "🇷🇺➡️🇪🇪 Переводчик русского и эстонского языков.\n\n"
        "Выберите действие:",
        reply_markup=main_keyboard,
    )

import random

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📖 Перевести":
        await update.message.reply_text("✍️ Напишите русское слово для перевода.")
        return

    if text == "🔍 Поиск":
        await update.message.reply_text("Введите слово для поиска.")
        return

    if text == "📚 Учить слова":
        ru = random.choice(list(dictionary.keys()))
        await update.message.reply_text(
            f"📖 Слово дня:\n\n🇷🇺 {ru}\n🇪🇪 {dictionary[ru]}"
        )
        return

    if text == "⭐ Избранное":
        await update.message.reply_text("⭐ Пока список избранного пуст.")
        return

    if text == "➕ Добавить слово":
        await update.message.reply_text(
            "Отправьте новое слово в формате:\n"
            "русское - эстонское"
        )
        return

    if text == "📊 Статистика":
        await update.message.reply_text(
            f"📚 В словаре сейчас {len(dictionary)} слов."
        )
        return

    if text == "⚙️ Настройки":
        await update.message.reply_text(
            "⚙️ Скоро здесь появятся настройки."
        )
        return

    if text == "ℹ️ Помощь":
        await update.message.reply_text(
            "Напишите русское слово — я переведу его на эстонский."
        )
        return

    word = text.lower().strip()

    if word in dictionary:
        await update.message.reply_text(
            f"🇷🇺 {word}\n🇪🇪 {dictionary[word]}"
        )
    else:
        await update.message.reply_text(
            "❌ Такого слова пока нет в словаре."
        )
        return

    word = text.lower()

    if word in dictionary:
        await update.message.reply_text(
            f"🇷🇺 {word}\n🇪🇪 {dictionary[word]}"
        )
    else:
        await update.message.reply_text("❌ Такого слова пока нет в словаре.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

print("EstoLex запущен...")
app.run_polling()
