import os
from telegram import Bot
from .streak_tracker import get_streak_days

async def post_to_channel(bot, progress_data):
    streak_days = get_streak_days()
    try:
        channel_id = os.getenv('CHANNEL_ID')
        if not channel_id:
            return False, "CHANNEL_ID not fount"

        hours, vocab, reading, writing, math, tests = progress_data

        message = (
            f"📊 Today's progress:\n\n"
            f"⏱ Time spent: {hours} hours\n"
            f"📚 Vocabulary: {vocab} words\n"
            f"📖 Reading: {reading} points\n"
            f"✍️ Writing: {writing} points\n"
            f"🧮 Mathematics: {math} points\n"
            f"📝 Tests: {tests} tests"
            f"\n\n"
            f"Day count {streak_days}"
        )

        await bot.send_message(chat_id=channel_id, text=message)
        return True, "Progress sent to channel"

    except Exception as e:
        return False, f"An error occurred: {str(e)}"
