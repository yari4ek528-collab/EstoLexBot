from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import random
from dictionary import dictionary

TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"

main_keyboard = ReplyKeyboardMarkup(
    [
        ["📖 Перевести"],
        ["📚 Учить слова"],
        ["📊 Статистика"],
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

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇪🇪 EstoLex\n\n"
        "Переводчик русского и эстонского языков.\n"
        "Версия: 1.0\n\n"
        "Создан для изучения эстонского языка."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Команды:\n\n"
        "/start — открыть меню\n"
        "/about — информация о боте\n"
        "/help — помощь\n\n"
        "Или просто отправьте русское слово для перевода."
    )

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📖 Перевести":
        await update.message.reply_text("✍️ Напишите русское слово для перевода.")
        return

    if text == "📚 Учить слова":
        ru = random.choice(list(dictionary.keys()))
        await update.message.reply_text(
            f"📖 Слово дня:\n\n🇷🇺 {ru}\n🇪🇪 {dictionary[ru]}"
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
        await help_command(update, context)
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

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

print("EstoLex запущен...")
app.run_polling()
