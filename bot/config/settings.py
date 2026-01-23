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
        
        # Groq API Key (required)
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            raise ValueError(
                "GROQ_API_KEY is not set. "
                "Please set it in your .env file or environment variables. "
                "Get a free key at: https://console.groq.com/keys"
            )
        
        # Groq Model (optional, defaults to llama-3.3-70b-versatile)
        self.groq_model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        
        # Bot configuration
        self.bot_name = "FIRST Robotics Mentor Bot"
        self.max_conversation_history = 10  # Number of messages to keep in context
    
    def __repr__(self):
        return (
            f"Settings(bot_name='{self.bot_name}', "
            f"groq_model='{self.groq_model}')"
        )


# Create a singleton settings instance
settings = Settings()
