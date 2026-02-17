from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from db import get_all
from config import BOT_TOKEN


async def start(update: Update, context):
    await update.message.reply_text("Бот работает. /data")


async def data(update: Update, context):
    rows = get_all()
    text = "\n".join([f"{r[1]} — {r[2]}₽" for r in rows[:10]])
    await update.message.reply_text(text or "Нет данных")


def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("data", data))
    app.run_polling()
