from telegram.ext import Updater, MessageHandler, Filters
from os import getenv

BOT_CHAT_ID = getenv("BOT_CHAT_ID")
BOT_TOKEN = getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]
canal = "@GGcompanyS3"

def mensaje(update, context):
    msg = update.message.text
    if update.effective_user.id in users_perm and str(msg).__contains__("/xd"):
        context.bot.delete_message(message_id = update.message.message_id, chat_id = update.message.chat_id)
        context.bot.send_message(chat_id = BOT_CHAT_ID, text = str(msg).replace("/xd", ""))
    if update.effective_user.id in users_perm and str(msg).__contains__("#s3"):
        context.bot.send_message(chat_id = canal, text = str(msg).replace("#s3", ""))

def fotos(update, context):
    imagen = update.message.photo[0].file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__("#s3"):
        comentario = str(comentario).replace("#s3", "")
        context.bot.send_photo(photo = imagen, chat_id = canal, caption = comentario)

def documento(update, context):
    documento = update.message.document.file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__("#s3"):
        comentario = str(comentario).replace("#s3", "")
        context.bot.send_document(chat_id = canal, document = documento, caption = comentario)

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, mensaje))
dp.add_handler(MessageHandler(Filters.photo, fotos))
dp.add_handler(MessageHandler(Filters.document, documento))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()