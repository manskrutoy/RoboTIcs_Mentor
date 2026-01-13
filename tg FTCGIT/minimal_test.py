"""Minimal bot test to isolate the issue."""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')

def main():
    # Replace with your actual token
    TOKEN = "8539941236:AAGIFGUnmEjPjMCYtCzxJfkavO0W9ChnvQU"
    
    logger.info("Creating application...")
    application = Application.builder().token(TOKEN).build()
    
    logger.info("Adding handler...")
    application.add_handler(CommandHandler("start", start))
    
    logger.info("Starting polling...")
    application.run_polling()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()
