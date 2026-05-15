# import dependencies
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from dotenv import load_dotenv
import os
import ai
import memory
import faq

# load our .env file
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Add website url only if required
faq.load(website_url='https://www.systemsltd.com/')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name

    # Each list inside keyboard = one horizontal row of buttons
    # Each InlineKeyboardButton has:
    #  text = what user sees on the button
    #  callaback_data = secret code sent to us whenever user presses the button
    keyboard = [
        [InlineKeyboardButton('💬 Start Chatting', callback_data='start_chat')],
        [InlineKeyboardButton('🔄 Reset Conversation', callback_data='reset')],
        [InlineKeyboardButton('ℹ️ About', callback_data='about')],
    ]

    # InlineKeyboardMarkup wraps the keyboard list into proper object
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Hello {name}! Welcome to our Customer Support Bot.\n\n"
        "I can help you with your questions anytime.\n\n"
        "Choose an option or just type your questions:",
        reply_markup=reply_markup # Attach Buttons to message
        )
    
# This function runs when Button is presses
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # query is the button press event
    query = update.callback_query

    # this tells telegram that we received the button press 
    await query.answer()

    user_id = query.from_user.id

    # query.data is the callback_data we set on each button
    if query.data == 'start_chat':
        await query.edit_message_text(
            "Great! Go ahead and type your question. I'm ready! 👂"
        )
    
    elif query.data == 'reset':
        await query.edit_message_text(
            "✅ Conversation cleared! Type /start to see the menu again."
        )
    
    elif query.data == 'about':
        await query.edit_message_text(
            "ℹ️ I'm an AI-powered support assistant by Nexora. \n\n"
            "I'm available 24/7 to answer your questions instantly. \n\n"
            "Type /start to go back to the menu."
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    # show "typing..." while we wait for AI response
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action='typing'
    )

    # get history using get_history function from memory module 
    history = memory.get_history(user_id)
    # Now we will ask for ai reply and passed history also to model
    reply = ai.get_ai_reply(user_message, history)

    # Save both messages(user, assistant) to memory using add_message func after getting reply
    memory.add_message(user_id, 'user', user_message)
    memory.add_message(user_id, 'assistant', reply)
    
    await update.message.reply_text(
    reply + "\n\n_💡 Tip: /start for menu • /reset to clear chat_",
    parse_mode="Markdown")

# /reset command clears conversation
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    memory.clear_history(user_id)

    await update.message.reply_text('✅ Conversation cleared! Start fresh.')



app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler('start',start))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()



