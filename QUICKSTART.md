# 🚀 Quick Start Guide

This is a simplified guide to get your bot running in **5 minutes**!

## Step 1: Get Your API Keys 🔑

### Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot`
3. Choose a name: `My FIRST Robotics Mentor`
4. Choose a username: `my_first_robotics_bot` (must end with `_bot`)
5. Copy the token that looks like: `1234567890:ABCdefGHI-jklMNOpqrsTUVwxyz`

### OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign in (or create account)
3. Click "Create new secret key"
4. Name it "Telegram Bot"
5. Copy the key that starts with `sk-`

## Step 2: Install Python Dependencies 📦

Open PowerShell in the project folder and run:

```powershell
cd "c:\Users\Берик\tg FTC"
pip install -r requirements.txt
```

## Step 3: Configure Your Bot ⚙️

1. **Copy the example file:**
   ```powershell
   copy .env.example .env
   ```

2. **Edit `.env` file** (open with Notepad):
   ```env
   TELEGRAM_BOT_TOKEN=paste_your_telegram_token_here
   OPENAI_API_KEY=paste_your_openai_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

3. **Save and close** the file

## Step 4: Run the Bot ▶️

```powershell
python -m bot.main
```

You should see:
```
INFO - Starting FIRST Robotics Mentor Bot...
INFO - Bot is starting polling...
```

> **Note:** Use `python -m bot.main` instead of `python bot/main.py` to ensure proper module imports.

## Step 5: Test in Telegram 💬

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. Try asking: "What is FIRST Robotics?"

## ✅ Success!

Your bot is now running! 🎉

**To stop the bot:** Press `Ctrl+C` in PowerShell

---

## Common Issues & Fixes 🔧

### "TELEGRAM_BOT_TOKEN is not set"
- Make sure `.env` file exists (not `.env.example`)
- Check there are no extra spaces in the file
- Token should be on the same line as `TELEGRAM_BOT_TOKEN=`

### "ModuleNotFoundError"
- Run: `pip install -r requirements.txt`
- Make sure you're in the correct folder

### Bot doesn't respond
- Check the bot is running (PowerShell window should be open)
- Type `/start` to initialize
- Check you're chatting with the right bot

### OpenAI errors
- Verify your API key is correct
- Make sure you have credits in your OpenAI account
- Try using `gpt-4o-mini` model (cheaper)

---

## Next Steps 🎯

Once your bot is working:

1. Try the `/learn` command to explore learning paths
2. Ask complex questions about robotics
3. Use `/clear` to reset conversation history
4. Customize the AI prompts in `bot/ai/prompts.py`

**Need more help?** See the full [README.md](README.md)
