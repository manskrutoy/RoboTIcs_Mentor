"""
Basic command handlers for the FIRST Robotics bot.
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /start command - welcome new users.
    """
    user_name = update.effective_user.first_name
    
    welcome_message = (
        f"👋 Hi {user_name}! Welcome to the **FIRST Robotics Mentor Bot**!\n\n"
        f"I'm here to help you learn about FIRST Robotics from the ground up. "
        f"Whether you're brand new to robotics or just getting started with your team, "
        f"I'll guide you through everything step by step! 🤖\n\n"
        f"**What I can help you with:**\n"
        f"• Understanding what FIRST Robotics is all about\n"
        f"• Learning robot basics (motors, sensors, mechanisms)\n"
        f"• Programming concepts for robotics\n"
        f"• Electronics and wiring\n"
        f"• Competition strategy\n"
        f"• Team roles and collaboration\n\n"
        f"**How to use me:**\n"
        f"• Type `/learn` to explore structured learning paths\n"
        f"• Type `/ask <your question>` to ask me anything\n"
        f"• Or just send me any message with a question!\n\n"
        f"Ready to start your robotics journey? Let's go! 🚀"
    )
    
    await update.message.reply_text(
        welcome_message,
        parse_mode="Markdown"
    )
    
    logger.info(f"User {update.effective_user.id} started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /help command - show available commands and usage.
    """
    help_message = (
        "📚 **FIRST Robotics Mentor Bot - Help**\n\n"
        "**Available Commands:**\n\n"
        "🏁 `/start` - Welcome message and introduction\n\n"
        "📖 `/learn` - Browse structured learning topics:\n"
        "   • Beginner basics (What is FIRST? Robot parts, Team roles)\n"
        "   • Intermediate topics (Programming, Electronics)\n"
        "   • Advanced topics (Strategy, Competition prep)\n\n"
        "❓ `/ask <question>` - Ask me any robotics question\n"
        "   Example: `/ask What is a motor controller?`\n\n"
        "💬 **Natural conversation:**\n"
        "You can also just send me any message and I'll respond!\n"
        "No need to use commands for every question.\n\n"
        "**Example questions to try:**\n"
        "• How does a robot move?\n"
        "• What's the difference between FRC and FTC?\n"
        "• Explain what autonomous mode is\n"
        "• How do I start learning to program a robot?\n\n"
        "**Tips:**\n"
        "✅ Ask simple questions to start\n"
        "✅ Tell me if you need more or less detail\n"
        "✅ Let me know your experience level\n\n"
        "I'm here to help you learn! Don't hesitate to ask anything. 😊"
    )
    
    await update.message.reply_text(
        help_message,
        parse_mode="Markdown"
    )
    
    logger.info(f"User {update.effective_user.id} requested help")


async def learn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /learn command - show structured learning paths.
    """
    keyboard = [
        [
            InlineKeyboardButton("🎯 Beginner", callback_data="learn_beginner"),
            InlineKeyboardButton("⚙️ Intermediate", callback_data="learn_intermediate"),
        ],
        [
            InlineKeyboardButton("🏆 Advanced", callback_data="learn_advanced"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    learn_message = (
        "📚 **Learning Paths**\n\n"
        "Choose your learning level to explore different topics:\n\n"
        "🎯 **Beginner** - New to robotics? Start here!\n"
        "   • What is FIRST Robotics?\n"
        "   • Robot basics and parts\n"
        "   • Team roles\n\n"
        "⚙️ **Intermediate** - Ready to dive deeper?\n"
        "   • Programming basics\n"
        "   • Electronics and wiring\n"
        "   • Robot mechanisms\n\n"
        "🏆 **Advanced** - Preparing for competition?\n"
        "   • Competition strategy\n"
        "   • Autonomous programming\n"
        "   • Advanced design\n\n"
        "Select a level below to get started! 👇"
    )
    
    await update.message.reply_text(
        learn_message,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
    
    logger.info(f"User {update.effective_user.id} opened learning paths")


async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /rules command - show FTC game manuals and resources.
    """
    rules_message = (
        "📜 **FTC Game Rules & Resources**\n\n"
        "Here are the official links for the current season:\n\n"
        "🎥 **Game Animation & Explanation:**\n"
        "[Watch Video](https://youtu.be/LCqWA6gSCXA?feature=shared)\n\n"
        "📖 **Official Game Manual:**\n"
        "[Read Manual](https://ftc-resources.firstinspires.org/ftc/game/manual)\n\n"
        "Make sure to read the manual carefully, especially the game rules part 1 and 2! 🤖"
    )
    
    await update.message.reply_text(
        rules_message,
        parse_mode="Markdown",
        disable_web_page_preview=False
    )
    
    logger.info(f"User {update.effective_user.id} requested rules")
