"""List available Gemini models."""
import os
import google.generativeai as genai
from bot.config import settings

def list_models():
    print(f"Listing models for key starting with: {settings.gemini_api_key[:5]}...")
    try:
        genai.configure(api_key=settings.gemini_api_key)
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Name: {m.name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_models()
