"""
Groq API client for ultra-fast AI responses.
Uses Groq's inference engine with OpenAI-compatible API.
"""

import logging
from typing import List, Dict
from groq import AsyncGroq
from bot.config import settings
from bot.ai.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class GroqClient:
    """Wrapper for Groq API with conversation context management."""
    
    def __init__(self):
        """Initialize the Groq client with API key from settings."""
        self.client = AsyncGroq(api_key=settings.groq_api_key)
        self.model = settings.groq_model
        logger.info(f"Groq client initialized with model: {self.model}")
    
    async def get_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]] = None,
        system_prompt: str = None
    ) -> str:
        """
        Get a response from the AI mentor using Groq.
        
        Args:
            user_message: The user's question or message
            conversation_history: Previous messages in the conversation
            system_prompt: Custom system prompt (uses default if not provided)
        
        Returns:
            The AI mentor's response as a string
        """
        try:
            # Use custom system prompt or default
            prompt = system_prompt or SYSTEM_PROMPT
            
            # Build messages array in OpenAI format
            messages = [{"role": "system", "content": prompt}]
            
            # Add conversation history if provided
            if conversation_history:
                messages.extend(conversation_history)
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Log the request
            logger.info(f"Sending request to Groq (model: {self.model})")
            
            # Call Groq API - super fast inference!
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,  # Balanced creativity and consistency
                max_tokens=1000,  # Reasonable length for Telegram
            )
            
            # Extract the response text
            assistant_message = response.choices[0].message.content
            
            # Log token usage
            logger.info(
                f"Groq response received. "
                f"Tokens used: {response.usage.total_tokens} "
                f"(prompt: {response.usage.prompt_tokens}, "
                f"completion: {response.usage.completion_tokens})"
            )
            
            return assistant_message
            
        except Exception as e:
            logger.error(f"Error calling Groq API: {e}")
            return (
                "Sorry, I'm having trouble connecting to my knowledge base right now. 😅\n\n"
                "Please try again in a moment, or use /help to see what else you can do!"
            )
    
    async def get_learning_response(
        self,
        topic_prompt: str,
        user_question: str = None
    ) -> str:
        """
        Get a response for a specific learning topic.
        
        Args:
            topic_prompt: The system prompt for this learning topic
            user_question: Optional follow-up question from the user
        
        Returns:
            The AI mentor's response
        """
        if user_question:
            message = user_question
        else:
            message = "Please teach me about this topic."
        
        return await self.get_response(
            user_message=message,
            system_prompt=topic_prompt
        )
