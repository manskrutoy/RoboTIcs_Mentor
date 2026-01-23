"""Test script for Gemini API."""
import os
import google.generativeai as genai
from bot.config import settings

def test_gemini():
    print("Testing Gemini API connection...")
    print(f"API Key present: {'Yes' if settings.gemini_api_key else 'No'}")
    print(f"Model: {settings.gemini_model}")
    
    try:
        genai.configure(api_key=settings.gemini_api_key)
        model = genai.GenerativeModel(settings.gemini_model)
        
        print("\nSending test prompt...")
        response = model.generate_content("Say hello!")
        print(f"\n✅ Success! Response: {response.text}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_gemini()
