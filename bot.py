from telegram.ext import Updater, MessageHandler, Filters
from os import getenv

BOT_CHAT_ID = getenv("BOT_CHAT_ID")
BOT_TOKEN = getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]

def mensaje(update, context):
    msg = update.message.text
    if update.effective_user.id in users_perm and str(msg).__contains__("/xd"):
        context.bot.delete_message(message_id = update.message.message_id, chat_id = update.message.chat_id)
        context.bot.send_message(chat_id = BOT_CHAT_ID, text = str(msg).replace("/xd", ""))
    elif update.effective_user.id in users_perm and str(msg).__contains__("#s3"):
        context.bot.send_message(chat_id = "@GGcompanyS3", text = str(msg).replace("#s3", ""))
    else:
        pass

def photo(update, context):
    if not update.effective_user['first_name'] == 'Telegram':
        caption = update.message.caption
        if update.effective_user.id in users_perm and str(caption).__contains__("#s3"):
            context.bot.send_photo(chat_id= "@canaldepruebaxdasdtumama", photo = update.message.message_id,caption = caption)

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, callback = mensaje))
dp.add_handler(MessageHandler(Filters.photo, callback = photo))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()