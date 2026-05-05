# import dependencies
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler,ContextTypes, filters
from dotenv import load_dotenv
import os
import ai

# load our .env file
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(f"Hello {name}! I am your support bot. \n\nAsk me anything!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    # show "typing..." while we wait for AI response
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action='typing'
    )

    # Now we will ask for ai reply
    reply = ai.get_ai_reply(user_message)
    
    await update.message.reply_text(reply)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler('start',start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()



