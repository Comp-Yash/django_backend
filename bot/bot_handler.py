import os
import django
import logging
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","notifyme.settings")
django.setup()

from bot.telegram_utils import link_telegram_user  

logging.basicConfig(level=logging.INFO)
TELEGRAM_BOT_TOKEN=config("TELEGRAM_BOT_TOKEN")


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    telegram_user=update.effective_user
    username=telegram_user.username
    telegram_id=telegram_user.id

    result_message=link_telegram_user(username,telegram_id)
    await update.message.reply_text(result_message)


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start",start))

    print("Telegram bot is Alive and Running")
    app.run_polling()
