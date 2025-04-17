
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
from handlers.handler import  start, report, graph, log_start, handle_log, mistake_start, handle_mistake


from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')

LOG, MISTAKE = range(2)


app = ApplicationBuilder().token(token).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("report", report))
app.add_handler(CommandHandler("graph", graph))

log_conv = ConversationHandler(
    entry_points=[CommandHandler('log', log_start)],
    states={LOG: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_log)]},
    fallbacks=[]
)

mistake_conv = ConversationHandler(
    entry_points=[CommandHandler('mistake', mistake_start)],
    states={MISTAKE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_mistake)]},
    fallbacks=[]
)

app.add_handler(log_conv)
app.add_handler(mistake_conv)
app.run_polling()
