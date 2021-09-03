from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]
canal = "@GGcompanyS3"
grupo = "-1001190361827"
enviar_grupo = "/xd"
enviar_canal = "#s3"

def mensaje(update, context):
    msg = update.message.text
    if update.effective_user.id in users_perm and str(msg).__contains__(enviar_grupo):
        context.bot.delete_message(message_id = update.message.message_id, chat_id = update.message.chat_id)
        context.bot.send_message(chat_id = grupo, text = str(msg).replace(enviar_grupo, ""))
    if update.effective_user.id in users_perm and str(msg).__contains__(enviar_canal):
        context.bot.send_message(chat_id = canal, text = str(msg).replace(enviar_canal, ""))

def fotos(update, context):
    imagen = update.message.photo[0].file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__(enviar_canal):
        comentario = str(comentario).replace(enviar_canal, "")
        context.bot.send_photo(photo = imagen, chat_id = canal, caption = comentario)

def documento(update, context):
    documento = update.message.document.file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__(enviar_canal):
        comentario = str(comentario).replace(enviar_canal, "")
        context.bot.send_document(chat_id = canal, document = documento, caption = comentario)

def promo(update, context):
    button_canal = InlineKeyboardButton("⛩CANAL⛩", url = "https://t.me/GGcompanyS3")
    button_grupo = InlineKeyboardButton("💬CHAT💬", url = "https://t.me/joinchatqM9TvYSDdxmMDUx")
    button_pxp1 = InlineKeyboardButton("📣PXP📣", url = "http://t.me/Kaneki59")
    button_pxp2 = InlineKeyboardButton("📢PXP📢", url = "http://t.me/D10S3GEEK")
    update.message.reply_text(text = "https://t.me/GGcompanyS3", reply_markup = InlineKeyboardMarkup([[button_canal, button_grupo],[button_pxp1],[button_pxp2]]))

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("promo", promo))
dp.add_handler(MessageHandler(Filters.text, mensaje))
dp.add_handler(MessageHandler(Filters.photo, fotos))
dp.add_handler(MessageHandler(Filters.document, documento))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()