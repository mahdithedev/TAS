import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "به موتور تبلیغ تلگرام خوش آمدید برای دریافت تبلیغ از دستور /getadd استفاده کنید"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6268117543:AAH6c92AiX0ulAjBRbUczbgAISvL5JF6UIM').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()