"""Test REST client for Gemini - List Models."""
import asyncio
import httpx
from bot.config import settings

async def test_list_models():
    print("Listing models via REST...")
    api_key = settings.gemini_api_key
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            for m in data.get('models', []):
                print(f"Name: {m['name']}")
                if 'generateContent' in m['supportedGenerationMethods']:
                    print(f"  - Supports generateContent")
        else:
            print(f"Error: {response.text}")

if __name__ == "__main__":
    asyncio.run(test_list_models())
