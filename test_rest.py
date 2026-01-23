"""Test REST client for Gemini."""
import asyncio
from bot.ai.gemini_client import GeminiClient

async def test_rest():
    print("Testing REST Client...")
    client = GeminiClient()
    
    print(f"URL: {client.api_url[:20]}...")
    
    response = await client.get_response("Hello! Are you working?")
    print(f"\nResponse:\n{response}")

if __name__ == "__main__":
    asyncio.run(test_rest())
