"""Test script to verify telegram bot imports and basic setup."""

import sys
print("Python version:", sys.version)

try:
    import telegram
    print(f"✓ telegram imported successfully, version: {telegram.__version__}")
except Exception as e:
    print(f"✗ telegram import failed: {e}")
    sys.exit(1)

try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler
    print("✓ telegram.ext imports successful")
except Exception as e:
    print(f"✗ telegram.ext import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    from bot.config import settings
    print(f"✓ bot.config.settings imported successfully")
    print(f"  Bot token length: {len(settings.telegram_bot_token)}")
    print(f"  OpenAI key length: {len(settings.openai_api_key)}")
    print(f"  Model: {settings.openai_model}")
except Exception as e:
    print(f"✗ bot.config import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n✅ All imports successful! Bot should be able to start.")
