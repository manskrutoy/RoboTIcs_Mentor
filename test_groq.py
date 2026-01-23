"""Quick test to verify Groq client works correctly."""

import asyncio
import logging
from bot.ai import GroqClient

# Set up logging
logging.basicConfig(level=logging.INFO)

async def test_groq():
    print("🚀 Testing Groq client initialization...")
    try:
        client = GroqClient()
        print("✅ Client initialized successfully!")
        print(f"   Model: {client.model}")
        
        print("\n🤖 Testing AI response...")
        response = await client.get_response("What is FIRST Robotics in one sentence?")
        print(f"✅ Response received:\n   {response[:150]}...")
        
        print("\n📚 Testing learning response...")
        learning_response = await client.get_learning_response(
            topic_prompt="You are teaching about robot mechanisms. Be concise.",
            user_question="What are the main types of mechanisms?"
        )
        print(f"✅ Learning response received:\n   {learning_response[:150]}...")
        
        print("\n✨ All tests passed! Groq is ready to use! 🎉")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_groq())
    exit(0 if success else 1)
