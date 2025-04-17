from utils.log_handler import log_progress
from utils.mistake_handler import add_mistake
from utils.report_generator import generate_report
from utils.graph_plotter import generate_graph
from utils.channel_post import post_to_channel
from utils.streak_tracker import get_streak_days
from telegram import Update
from telegram.ext import  CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

LOG, MISTAKE = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    streak_days = get_streak_days()

    streak_message = ""
    if streak_days > 0:
        streak_message = f"🔥 Strict Days: {streak_days} !\n\n"


    await update.message.reply_text(f"{streak_message}\nCommands:\n/log - Log your daily progress\n/mistake - Add a mistake\n/report - Get weekly summary\n/graph - Show progress graph")

async def log_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your log in this format:\nhours vocab reading writing math tests\nExample: 15 30 27 24 33 1")
    return LOG

async def handle_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        vals = list(map(int, update.message.text.strip().split()))
        log_progress(*vals)

        success, message = await post_to_channel(context.bot, vals)

        if success:
            await update.message.reply_text("Progress saved and posted to channel!")
        else:
            await update.message.reply_text(f"Progress saved! But couldn't post to channel: {message}")
    except:
        await update.message.reply_text("Invalid format. Try again.")
    return ConversationHandler.END

async def mistake_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send mistake as:\nsection question error_type note\nExample: Reading 12 vocab 'did not know compelling'")
    return MISTAKE

async def handle_mistake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip().split(' ', 3)
        add_mistake(*text)
        await update.message.reply_text("Mistake saved!")
    except:
        await update.message.reply_text("Invalid format.")
    return ConversationHandler.END

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = generate_report()
    await update.message.reply_text(text)

async def graph(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = generate_graph()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'))
