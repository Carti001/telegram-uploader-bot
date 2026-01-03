import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nفایل بفرست آپلودش کنم")

async def uploader(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document:
        await update.message.reply_text("فایل دریافت شد ✅")
    else:
        await update.message.reply_text("فقط فایل بفرست 📁")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, uploader))
    app.run_polling()

if __name__ == "__main__":
    main()
