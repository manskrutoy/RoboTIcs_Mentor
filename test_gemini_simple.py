"""Test script for Gemini API with hardcoded model."""
import google.generativeai as genai
from bot.config import settings

def test_gemini():
    print(f"Testing Gemini API with key: {settings.gemini_api_key[:5]}...")
    
    try:
        genai.configure(api_key=settings.gemini_api_key)
        # Try specific model name
        model_name = "gemini-1.5-flash"
        print(f"Using model: {model_name}")
        model = genai.GenerativeModel(model_name)
        
        print("Sending 'Hello'...")
        response = model.generate_content("Hello")
        print(f"✅ Success! Response: {response.text}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_gemini()
