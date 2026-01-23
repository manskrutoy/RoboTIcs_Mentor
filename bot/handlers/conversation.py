"""
Conversation handlers for natural interaction with the AI mentor.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from bot.ai import GroqClient
from bot.config import settings

logger = logging.getLogger(__name__)

# Initialize Groq client
ai_client = GroqClient()

# User conversation contexts stored in memory
# Format: {user_id: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
user_contexts = {}


async def ask_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /ask command - answer a specific question.
    Usage: /ask <question>
    """
    # Get the question from command arguments
    if not context.args:
        await update.message.reply_text(
            "❓ **How to use /ask:**\n\n"
            "Type `/ask` followed by your question!\n\n"
            "**Example:**\n"
            "`/ask What is a motor controller?`\n\n"
            "Or just send me any message without a command! 😊",
            parse_mode="Markdown"
        )
        return
    
    question = " ".join(context.args)
    
    # Process the question
    await process_user_message(update, question)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle regular messages as questions to the AI mentor.
    This is called for any message that doesn't match a command.
    """
    user_message = update.message.text
    
    # Ignore empty messages
    if not user_message or not user_message.strip():
        return
    
    await process_user_message(update, user_message)


async def process_user_message(update: Update, user_message: str):
    """
    Process a user's message and generate an AI response.
    Manages conversation context and history.
    """
    user_id = update.effective_user.id
    
    # Show typing indicator in the header
    await update.message.chat.send_action("typing")
    
    # Send a "Thinking" placeholder message
    placeholder_msg = await update.message.reply_text(
        "🤔 **Thinking...**\n_Generating mentor response..._",
        parse_mode="Markdown"
    )
    
    try:
        # Get or create conversation context for this user
        if user_id not in user_contexts:
            user_contexts[user_id] = []
        
        conversation_history = user_contexts[user_id]
        
        # Get AI response with conversation context
        response = await ai_client.get_response(
            user_message=user_message,
            conversation_history=conversation_history
        )
        
        # Update conversation history
        conversation_history.append({"role": "user", "content": user_message})
        conversation_history.append({"role": "assistant", "content": response})
        
        # Trim history to max length to avoid token limits
        max_history = settings.max_conversation_history * 2
        if len(conversation_history) > max_history:
            conversation_history = conversation_history[-max_history:]
        
        user_contexts[user_id] = conversation_history
        
        # Edit the placeholder with the final response
        await placeholder_msg.edit_text(response, parse_mode="Markdown")
        
        logger.info(
            f"User {user_id} asked: '{user_message[:50]}...' "
            f"(history length: {len(conversation_history)})"
        )
        
    except Exception as e:
        logger.error(f"Error processing message from user {user_id}: {e}")
        error_text = (
            "😅 Oops! Something went wrong while thinking. Please try asking again!\n\n"
            "If this keeps happening, try using /start to reset our conversation."
        )
        await placeholder_msg.edit_text(error_text, parse_mode="Markdown")


async def clear_context_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Clear the conversation context for a user.
    Usage: /clear
    """
    user_id = update.effective_user.id
    
    if user_id in user_contexts:
        del user_contexts[user_id]
    
    await update.message.reply_text(
        "✅ Conversation history cleared! We're starting fresh. 🔄\n\n"
        "What would you like to learn about?",
        parse_mode="Markdown"
    )
    
    logger.info(f"User {user_id} cleared conversation context")
