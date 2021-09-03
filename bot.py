from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]
channel_id = "@GGcompanyS3"
group_id = "-1001190361827"
for_group = "/xd"
for_channel = "#s3"

def start(update, context):
    update.message.reply_text(f"Hola <b>{update.effective_user.first_name}-sama</b>, que puedo hacer por ti?\n\n"
    "<b>Ayuda del bot:</b>\n/xd - Envia un mensaje al grupo.\n#s3 - Envia un mensaje al canal.\n/p - Envia el mensaje de promo al usuario.\n/pc - Envia el mensaje de promo al canal.", parse_mode = "html")

def messages(update, context):
    msg = update.message.text
    if update.effective_user.id in users_perm and str(msg).__contains__(for_group):
        context.bot.delete_message(message_id = update.message.message_id, chat_id = update.message.chat_id)
        context.bot.send_message(chat_id = group_id, text = str(msg).replace(for_group, ""))
    if update.effective_user.id in users_perm and str(msg).__contains__(for_channel):
        context.bot.send_message(chat_id = channel_id, text = str(msg).replace(for_channel, ""))

def photo_to_channel(update, context):
    imagen = update.message.photo[0].file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__(for_channel):
        comentario = str(comentario).replace(for_channel, "")
        context.bot.send_photo(photo = imagen, chat_id = channel_id, caption = comentario)

def document_to_channel(update, context):
    documento = update.message.document.file_id
    comentario = update.message.caption
    if update.effective_user.id in users_perm and str(comentario).__contains__(for_channel):
        comentario = str(comentario).replace(for_channel, "")
        context.bot.send_document(chat_id = channel_id, document = documento, caption = comentario)

button_channel = InlineKeyboardButton("⛩CANAL⛩", url = "https://t.me/GGcompanyS3")
button_group = InlineKeyboardButton("💬CHAT💬", url = "https://t.me/joinchatqM9TvYSDdxmMDUx")
button_pxp1 = InlineKeyboardButton("📣PXP📣", url = "http://t.me/Kaneki59")
button_pxp2 = InlineKeyboardButton("📢PXP📢", url = "http://t.me/D10S3GEEK")

def send_channel(update, context):
    if update.effective_user.id in users_perm:
        context.bot.send_message(chat_id = channel_id, text = "https://t.me/GGcompanyS3", reply_markup = InlineKeyboardMarkup([[button_channel, button_group], [button_pxp1], [button_pxp2]]))

def send_user(update, context):
    if update.effective_user.id in users_perm:
        update.message.reply_text("https://t.me/GGcompanyS3", reply_markup = InlineKeyboardMarkup([[button_channel, button_group], [button_pxp1], [button_pxp2]]))

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("p", send_user))
dp.add_handler(CommandHandler("pc", send_channel))
dp.add_handler(MessageHandler(Filters.text, messages))
dp.add_handler(MessageHandler(Filters.photo, photo_to_channel))
dp.add_handler(MessageHandler(Filters.document, document_to_channel))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()