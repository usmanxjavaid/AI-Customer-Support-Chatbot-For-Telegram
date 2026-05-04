# import dependencies
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Telegram bot token
# TELEGRAM_TOKEN = 

# Below function runs when someone types /start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update.effective_user is the person who sent the message
    name = update.effective_user.first_name

    # update.message.reply_text sends back reply to a person
    await update.message.reply_text(f"Hello {name}! I am Customer support Chatbot by Nexora. How can i help you?")

# Below function will run when user sens any normal message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You Said: {user_message}")


# Create the bot application object
try:
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    print("Bot initialized successfully!")
except Exception as e:
    print(f"Failed to initialize bot: {e}")
    exit(1)

# When someone types /start, call the start function
app.add_handler(CommandHandler('start', start))

# this will ignore commands (e.g. /start) and trigger normal messages 
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


# Start listening for messages
app.run_polling()
