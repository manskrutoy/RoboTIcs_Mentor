"""
Groq API client for fast LLM inference.
Compatible with the existing AI client interface.
"""

import logging
from typing import List, Dict
from groq import Groq
from bot.config import settings

logger = logging.getLogger(__name__)


class GroqClient:
    """Wrapper for Groq API."""
    
    def __init__(self):
        """Initialize the Groq client."""
        self.api_key = settings.groq_api_key
        self.client = Groq(api_key=self.api_key)
        self.model = settings.groq_model if settings.groq_model else "llama-3.3-70b-versatile"
        
        logger.info(f"Groq client initialized with model: {self.model}")
    
    async def get_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]] = None,
        system_prompt: str = None
    ) -> str:
        """Get response from Groq."""
        try:
            # Build messages array for chat completion
            messages = []
            
            # Add system prompt if provided
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            else:
                # Default system prompt for FIRST Robotics mentor
                messages.append({
                    "role": "system",
                    "content": (
                        "You are a helpful and knowledgeable mentor for FIRST Tech Challenge (FTC) robotics. "
                        "Provide clear, educational responses about robotics, programming, engineering, and teamwork. "
                        "Be encouraging and supportive while being technically accurate."
                    )
                })
            
            # Add conversation history (last 6 messages to avoid token limits)
            if conversation_history:
                for msg in conversation_history[-6:]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
            
            # Add current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
            )
            
            if response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                return "I couldn't generate a response."
            
        except Exception as e:
            logger.error(f"Error calling Groq API: {e}")
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
