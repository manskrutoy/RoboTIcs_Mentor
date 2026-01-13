"""
Configuration settings for the FIRST Robotics Telegram bot.
Loads environment variables and validates required settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """Application settings loaded from environment variables."""
    
    def __init__(self):
        # Telegram Bot Token (required)
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not self.telegram_bot_token:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN is not set. "
                "Please set it in your .env file or environment variables."
            )
        
        # Google Gemini API Key (required)
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Please set it in your .env file or environment variables. "
                "Get a free key at: https://aistudio.google.com/app/apikey"
            )
        
        # Gemini Model (optional, defaults to gemini-2.5-flash)
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        
        # Bot configuration
        self.bot_name = "FIRST Robotics Mentor Bot"
        self.max_conversation_history = 10  # Number of messages to keep in context
    
    def __repr__(self):
        return (
            f"Settings(bot_name='{self.bot_name}', "
            f"gemini_model='{self.gemini_model}')"
        )


# Create a singleton settings instance
settings = Settings()
