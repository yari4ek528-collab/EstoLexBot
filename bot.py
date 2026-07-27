from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8847485249:AAFFUi2oRcHYCE03YFHr20cwL64rKoj0DiM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
