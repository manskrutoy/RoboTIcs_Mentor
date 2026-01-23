import asyncio
import os
import logging
from bot.ai.gemini_client import GeminiClient
from bot.config import settings

# Configure logging to print to console
logging.basicConfig(level=logging.INFO)

async def reproduce():
    print(f"Testing Gemini Client...")
    print(f"API Key start: {settings.gemini_api_key[:5] if settings.gemini_api_key else 'None'}")
    print(f"Model: {settings.gemini_model}")
    
    client = GeminiClient()
    response = await client.get_response("Hello, are you working?")
    print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(reproduce())
