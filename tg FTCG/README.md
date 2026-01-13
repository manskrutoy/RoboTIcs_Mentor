# 🤖 FIRST Robotics Mentor Bot

A friendly Telegram bot powered by OpenAI that helps beginners learn FIRST Robotics concepts through conversational AI mentorship.

## 📋 Overview

This bot acts as a personal robotics mentor for students aged 13-18 who are new to FIRST Robotics. It provides:

- ✅ Interactive learning paths (Beginner → Intermediate → Advanced)
- ✅ AI-powered Q&A for any robotics question
- ✅ Structured lessons on robot design, programming, electronics, and strategy
- ✅ Friendly, encouraging mentorship tone
- ✅ Context-aware conversations that remember your questions

## 🚀 Features

### Commands

- `/start` - Get welcomed and learn how to use the bot
- `/help` - See all available commands and usage examples
- `/learn` - Browse structured learning topics by difficulty level
- `/ask <question>` - Ask any robotics question
- `/clear` - Clear your conversation history and start fresh

### Learning Paths

**🎯 Beginner Topics:**
- What is FIRST Robotics?
- Robot parts and basics
- Team roles and collaboration

**⚙️ Intermediate Topics:**
- Programming basics for robotics
- Electronics and wiring
- Robot mechanisms

**🏆 Advanced Topics:**
- Competition strategy
- Autonomous programming
- Advanced robot design

### Natural Conversation

Just send any message to the bot, and it will answer like a friendly mentor! No need to use commands for every question.

## 🛠️ Prerequisites

Before you start, make sure you have:

1. **Python 3.9 or higher** - [Download Python](https://www.python.org/downloads/)
2. **A Telegram account**
3. **OpenAI API key** - [Get one here](https://platform.openai.com/api-keys)
4. **Telegram Bot Token** - Instructions below

## 📦 Installation

### Step 1: Clone or Download This Project

```bash
cd "c:\Users\Берик\tg FTC"
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

### Step 1: Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` to create a new bot
3. Follow the prompts to choose a name and username for your bot
4. BotFather will give you a **Bot Token** - save this!

Example token format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 2: Get an OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key - you won't be able to see it again!

### Step 3: Create Your `.env` File

1. Copy the `.env.example` file:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` in a text editor (Notepad, VS Code, etc.)

3. Add your API keys:
   ```env
   TELEGRAM_BOT_TOKEN=your_actual_telegram_token_here
   OPENAI_API_KEY=your_actual_openai_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

4. Save the file

**⚠️ Important:** Never share your `.env` file or commit it to Git! It contains secret keys.

## ▶️ Running the Bot

### Start the Bot

```bash
python -m bot.main
```

You should see output like:
```
2026-01-10 23:50:00 - __main__ - INFO - Starting FIRST Robotics Mentor Bot...
2026-01-10 23:50:00 - __main__ - INFO - Bot is starting polling...
```

### Test the Bot

1. Open Telegram
2. Search for your bot by the username you created
3. Send `/start` to begin
4. Try asking: "What is FIRST Robotics?"

### Stop the Bot

Press `Ctrl+C` in the terminal to stop the bot gracefully.

## 💬 Usage Examples

Here are some example interactions:

### Using Commands

```
/start
👋 Hi Alex! Welcome to the FIRST Robotics Mentor Bot!

/ask What is a motor controller?
🤔 Great question! A motor controller is like a "smart switch" for your robot's motors...

/learn
📚 Learning Paths
Choose your learning level to explore different topics...
```

### Natural Conversation

```
You: How does a robot move?

Bot: Great question! Let me break down how robots move...

You: What about turning?

Bot: Good follow-up! Turning depends on your robot's drivetrain type...
```

## 🧪 Troubleshooting

### "TELEGRAM_BOT_TOKEN is not set"

- Make sure you created a `.env` file (not `.env.example`)
- Check that there are no spaces around the `=` sign
- Make sure the token is correct

### "Error calling OpenAI API"

- Verify your OpenAI API key is correct
- Check that you have credits in your OpenAI account
- Try switching to `gpt-4o-mini` in `.env` for lower costs

### Bot doesn't respond

- Make sure the bot is running (check the terminal)
- Verify you're messaging the correct bot
- Try `/start` to reset

### "Module not found" errors

- Make sure you installed dependencies: `pip install -r requirements.txt`
- Check that your virtual environment is activated

## 📁 Project Structure

```
tg FTC/
├── bot/
│   ├── __init__.py
│   ├── main.py                 # Main bot entry point
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── commands.py         # /start, /help, /learn commands
│   │   ├── conversation.py     # Message handling and /ask
│   │   └── learning_paths.py   # Interactive learning topics
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── openai_client.py    # OpenAI API integration
│   │   └── prompts.py          # AI mentor personality
│   └── config/
│       ├── __init__.py
│       └── settings.py         # Configuration management
├── .env                         # Your API keys (create this!)
├── .env.example                 # Template for .env
├── .gitignore
├── requirements.txt
└── README.md                    # This file
```

## 🔒 Security Notes

- **Never share your `.env` file**
- **Never commit `.env` to Git** (it's in `.gitignore`)
- Keep your API keys private
- Regenerate keys if they're exposed

## 💰 Cost Considerations

This bot uses OpenAI's API, which charges per token:

- **gpt-4o-mini**: ~$0.00015 per 1K tokens (very cheap)
- **gpt-4o**: ~$0.005 per 1K tokens (more expensive but smarter)

For learning purposes, `gpt-4o-mini` is recommended and costs just a few cents for hundreds of questions.

## 🤝 Contributing

Want to improve this bot? Ideas:

- Add more learning topics
- Implement quizzes or challenges
- Add support for images/diagrams
- Create a database for conversation persistence
- Add team collaboration features

## 📝 License

This project is open source and available for educational purposes.

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the logs in your terminal
3. Make sure all prerequisites are installed
4. Verify your API keys are correct

## 🎓 Learning Resources

- [FIRST Robotics Official Site](https://www.firstinspires.org/)
- [FRC Documentation](https://docs.wpilib.org/)
- [FTC Documentation](https://ftc-docs.firstinspires.org/)
- [python-telegram-bot Documentation](https://docs.python-telegram-bot.org/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)

---

**Happy learning, and good luck with your robotics journey! 🤖🚀**
