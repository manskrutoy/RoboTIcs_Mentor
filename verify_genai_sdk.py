from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def test_new_sdk():
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"Testing with API key: {api_key[:10]}...")
    
    client = genai.Client(api_key=api_key)
    
    print("\n--- Listing Models ---")
    try:
        for model in client.models.list():
            print(f"- {model.name}")
    except Exception as e:
        print(f"Error listing models: {e}")

    test_models = ["gemini-1.5-flash", "gemini-2.0-flash-exp"]
    
    # Add whatever the user thinks they have
    test_models.append("gemini-2.5-flash") 

    for model_id in test_models:
        print(f"\n--- Testing Model: {model_id} ---")
        try:
            response = client.models.generate_content(
                model=model_id,
                contents="Say 'System Online'"
            )
            print(f"Success! Response: {response.text}")
        except Exception as e:
            print(f"Failed for {model_id}: {e}")

if __name__ == "__main__":
    test_new_sdk()
