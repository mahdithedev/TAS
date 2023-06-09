import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from random import randint

# for test only remove for production
authentication_list = []
authenticated_users = []

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def generate_random_code(length):

    code = ""

    for i in range(length):
        code += str(randint(0 , 9))

    return code

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "به موتور تبلیغ تلگرام خوش آمدید برای دریافت تبلیغ از دستور /getadd استفاده کنید"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
    auth_code = generate_random_code(4)
    channel_name = context.args[0]
    authentication_list.append(auth_code , channel_name)
    await context.bot.send_message(chat_id=update.effective_chat.id , text=auth_code)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6268117543:AAH6c92AiX0ulAjBRbUczbgAISvL5JF6UIM').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()