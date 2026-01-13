"""
Main entry point for the FIRST Robotics Telegram Bot.
"""

import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from bot.config import settings
from bot.handlers import (
    start_command,
    help_command,
    learn_command,
    ask_command,
    handle_message,
    handle_learning_callback,
)
from bot.handlers.conversation import clear_context_command

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    logger.info("Starting FIRST Robotics Mentor Bot...")
    logger.info(f"Configuration: {settings}")
    
    # Start keep-alive server (for platforms like Render/Railway)
    # Only needed if PORT environment variable is set
    import os
    if "PORT" in os.environ:
        from bot import keep_alive
        keep_alive.start()
    
    # Create the Application
    application = Application.builder().token(settings.telegram_bot_token).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("learn", learn_command))
    application.add_handler(CommandHandler("ask", ask_command))
    application.add_handler(CommandHandler("clear", clear_context_command))
    
    # Register callback query handler for interactive buttons
    application.add_handler(CallbackQueryHandler(handle_learning_callback))
    
    # Register message handler for natural conversation
    # This catches all text messages that don't match commands
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    
    # Start the bot
    logger.info("Bot is starting polling...")
    application.run_polling()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise
