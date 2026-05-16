import database
from telegram import Update
from telegram.ext import ContextTypes
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()
ADMIN_ID = int(os.getenv('ADMIN_ID', 0))

# define a function for an admin check
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('⛔ Access denied.')
        return
    
    # Get stats from database
    total_users, total_messages = database.get_stats()

    await update.message.reply_text(
        f"📊 *Admin Panel*\n\n"
        f"👥 Total Users: {total_users}\n"
        f"💬 Total Messages: {total_messages}\n",
        parse_mode="Markdown"
    )

async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Access denied.")
        return
    
    all_users = database.get_all_users()

    if not all_users:
        await update.message.reply_text("No users yet.")
        return
    
    msg = "👥 *All Users*\n\n"
    for u in all_users:
        telegram_id, first_name, username, joined_at = u
        msg += f"First Name*{first_name}*"
        msg += f"\nUsername(@{username})" if username else""
        msg += f"\n ID: `{telegram_id}`"
        msg += f"\n Joined: {joined_at}\n\n"

    await update.message.reply_text(msg, parse_mode="Markdown")

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Access denied.")
        return
    
    if not context.args:
        await update.message.reply_text(
            "Please provide a user ID.\nExample: `/history 123456`",
            parse_mode='Markdown'
        )
        return
    
    telegram_id = int(context.args[0])
    messages = database.get_user_conversations(telegram_id)

    if not messages:
        await update.message.reply_text('No conversations found for this user.')
        return
    
    msg = f"💬 *Conversation History*\n `ID: {telegram_id}`\n\n"
    for role, message, timestamp in messages[-10:]:
        icon = "👤" if role == "user" else "🤖"
        msg += f"{icon} {message}\n_{timestamp}_\n\n"

    await update.message.reply_text(msg, parse_mode='Markdown')










