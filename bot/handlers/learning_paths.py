"""
Learning path handlers with interactive topic navigation.
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.ai import GroqClient
from bot.ai.prompts import get_learning_path_prompt

logger = logging.getLogger(__name__)

# Initialize Groq client
ai_client = GroqClient()


# Learning content topics
LEARNING_TOPICS = {
    "beginner": {
        "title": "🎯 Beginner Topics",
        "topics": [
            ("What is FIRST?", "basics_what_is_first"),
            ("Robot Parts", "basics_robot_parts"),
            ("Team Roles", "basics_team_roles"),
        ],
    },
    "intermediate": {
        "title": "⚙️ Intermediate Topics",
        "topics": [
            ("Programming Basics", "programming_basics"),
            ("Electronics & Wiring", "electronics_basics"),
            ("Robot Mechanisms", "mechanisms_basics"),
        ],
    },
    "advanced": {
        "title": "🏆 Advanced Topics",
        "topics": [
            ("Competition Strategy", "competition_strategy"),
            ("Autonomous Mode", "autonomous_programming"),
            ("Advanced Design", "advanced_design"),
        ],
    },
}


async def handle_learning_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle callback queries from inline keyboard buttons.
    """
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    # Handle level selection (beginner, intermediate, advanced)
    if callback_data.startswith("learn_"):
        level = callback_data.replace("learn_", "")
        await show_topic_menu(query, level)
    
    # Handle topic selection
    elif callback_data.startswith("topic_"):
        topic_id = callback_data.replace("topic_", "")
        await show_topic_content(query, topic_id)
    
    # Handle back navigation
    elif callback_data == "back_to_levels":
        await show_learning_levels(query)


async def show_learning_levels(query):
    """Show the main learning level selection menu."""
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
    
    message = (
        "📚 **Learning Paths**\n\n"
        "Choose your learning level:\n\n"
        "🎯 **Beginner** - New to robotics\n"
        "⚙️ **Intermediate** - Ready to dive deeper\n"
        "🏆 **Advanced** - Competition preparation\n\n"
        "Select a level below! 👇"
    )
    
    await query.edit_message_text(
        message,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


async def show_topic_menu(query, level: str):
    """
    Show the topic selection menu for a specific learning level.
    """
    if level not in LEARNING_TOPICS:
        await query.edit_message_text("❌ Invalid learning level.")
        return
    
    level_data = LEARNING_TOPICS[level]
    title = level_data["title"]
    topics = level_data["topics"]
    
    # Create buttons for each topic
    keyboard = []
    for topic_name, topic_id in topics:
        keyboard.append([
            InlineKeyboardButton(topic_name, callback_data=f"topic_{topic_id}")
        ])
    
    # Add back button
    keyboard.append([
        InlineKeyboardButton("⬅️ Back to Levels", callback_data="back_to_levels")
    ])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"{title}\n\nSelect a topic to learn about:"
    
    await query.edit_message_text(
        message,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
    
    logger.info(f"User {query.from_user.id} browsing {level} topics")


async def show_topic_content(query, topic_id: str):
    """
    Show the AI-generated content for a specific topic.
    """
    # Show loading message with "animation"
    await query.edit_message_text(
        "🧠 **Mentor is thinking...**\n\n_Preparing your robotics lesson..._ 🤖",
        parse_mode="Markdown"
    )
    
    try:
        # Get the appropriate prompt for this topic
        topic_prompt = get_learning_path_prompt(topic_id)
        
        # Get AI response
        response = await ai_client.get_learning_response(
            topic_prompt=topic_prompt
        )
        
        # Create back button
        keyboard = [[
            InlineKeyboardButton("⬅️ Back to Topics", callback_data=f"learn_{get_level_from_topic(topic_id)}")
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send the response
        await query.edit_message_text(
            response,
            parse_mode="Markdown",
            reply_markup=reply_markup
        )
        
        logger.info(f"User {query.from_user.id} learned about {topic_id}")
        
    except Exception as e:
        logger.error(f"Error generating topic content: {e}")
        await query.edit_message_text(
            "❌ Sorry, I had trouble generating the content. Please try again!",
            parse_mode="Markdown"
        )


def get_level_from_topic(topic_id: str) -> str:
    """Determine which level a topic belongs to."""
    for level, data in LEARNING_TOPICS.items():
        for _, tid in data["topics"]:
            if tid == topic_id:
                return level
    return "beginner"  # Default fallback
