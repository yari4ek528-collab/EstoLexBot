from telegram import Update
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Добро пожаловать в EstoLex!\n\n"
        "Напишите русское слово, и я переведу его на эстонский."
    )

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = update.message.text.lower().strip()

    if word in dictionary:
        await update.message.reply_text(
            f"🇷🇺 {word}\n🇪🇪 {dictionary[word]}"
        )
    else:
        await update.message.reply_text(
            "❌ Такого слова пока нет в словаре."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

app.run_polling()
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = update.message.text.lower().strip()

    print(f"Получено: {word}")

    translation = dictionary.get(word)

    if translation:
        await update.message.reply_text(f"🇷🇺 {word}\n🇪🇪 {translation}")
    else:
        await update.message.reply_text(
            f"❌ Слово «{word}» пока отсутствует в словаре."
)
