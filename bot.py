from telegram.ext import Updater, MessageHandler, Filters
from os import getenv


BOT_CHAT_ID = "-1001190361827"#getenv("BOT_CHAT_ID")
BOT_TOKEN = "1918486207:AAFmafmHIfCsbQds9r_41wuvES8H8gqyjCc"#getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]
s = "/xd"

def mensaje(update, context):
    msg = update.message.text
    if update.effective_user.id in users_perm and str(msg).__contains__(s):
        context.bot.delete_message(message_id = update.message.message_id, chat_id = update.message.chat_id)
        context.bot.send_message(chat_id = BOT_CHAT_ID, text = str(msg).replace(s, ""))

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, callback = mensaje))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()