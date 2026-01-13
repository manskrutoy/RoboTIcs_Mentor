"""
Google Gemini API client using the new google-genai SDK.
Verified for Gemini 1.5+ and 2.0+ models.
"""

import logging
from typing import List, Dict
from google import genai
from bot.config import settings

logger = logging.getLogger(__name__)


class GeminiClient:
    """Wrapper for Google Gemini API using new SDK."""
    
    def __init__(self):
        """Initialize the Gemini client."""
        self.api_key = settings.gemini_api_key
        # Initialize client with API key
        self.client = genai.Client(api_key=self.api_key)
        
        # Use settings model or fallback to gemini-1.5-flash
        self.model = settings.gemini_model if settings.gemini_model else "gemini-1.5-flash"
        
        # The new SDK typically expects models without "models/" prefix,
        # but handles verification dynamically. We strip it to be safe.
        if self.model.startswith("models/"):
            self.model = self.model.replace("models/", "")
            
        logger.info(f"Gemini client initialized with model: {self.model}")
    
    async def get_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]] = None,
        system_prompt: str = None
    ) -> str:
        """Get response from Gemini."""
        try:
            # Construct simplified prompt for chat
            full_prompt = ""
            if system_prompt:
                # Add system prompt at the start
                full_prompt += f"System Instructions: {system_prompt}\n\n"
            
            if conversation_history:
                pass # For now, let's keep it simple and stateless to avoid errors
                # But we can add history if needed:
                for msg in conversation_history[-6:]:
                    role = "User" if msg["role"] == "user" else "Model"
                    full_prompt += f"{role}: {msg['content']}\n"
            
            full_prompt += f"User: {user_message}\nModel:"
            
            # Use the simple generate_content method
            response = self.client.models.generate_content(
                model=self.model,
                contents=full_prompt
            )
            
            if response.text:
                return response.text
            else:
                return "I couldn't generate a text response."
            
        except Exception as e:
            logger.error(f"Error calling Gemini API (google-genai): {e}")
            return (
                "Sorry, I'm having trouble connecting to my knowledge base right now. 😅\n"
                "Please try again in a moment."
            )
    
    async def get_learning_response(
        self,
        topic_prompt: str,
        user_question: str = None
    ) -> str:
        """Get learning content."""
        message = user_question if user_question else "Please teach me about this topic."
        return await self.get_response(user_message=message, system_prompt=topic_prompt)
