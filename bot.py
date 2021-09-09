from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")

users_perm = [1816693475, 1325010317]
channel_id = "@GGcompanyS3"
group_id = "-1001190361827"
for_group = "/xd"
for_channel = "#s3"

VIDEO_PROMO = "https://tgfilestorage.com/dl_8345781/gif.mp4"

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
button_pxp1 = InlineKeyboardButton("📢PXP1📢", url = "http://t.me/Kaneki59")
button_pxp2 = InlineKeyboardButton("📢PXP2📢", url = "http://t.me/D10S3GEEK")
button_admin = InlineKeyboardButton("💫QUIERO SER ADMIN💫", url = "http://t.me/D10S3GEEK")
button_aportes1 = InlineKeyboardButton("🤝APORTES🤝", url = "http://t.me/Kaneki59")
button_aportes2 = InlineKeyboardButton("🤝APORTES🤝", url = "http://t.me/D10S3GEEK")

def send_channel(update, context):
    if update.effective_user.id in users_perm:
        context.bot.send_video(chat_id = channel_id, video = VIDEO_PROMO, 
        caption = "Grupo 👥 creado con el objetivo de q los usuarios 👤 de este canal puedan disfrutar de diversos 🤳 contenidos sin que se vean afectados 📈 sus paquete de datos móviles (total mente gratis)🚫💸\n\n● Juegos🕹\n● Series 🎥\n● Anime ⛩\n● Humor 😂",
        reply_markup = InlineKeyboardMarkup([[button_channel, button_group], [button_pxp1], [button_pxp2], [button_admin], [button_aportes1, button_aportes2]]))

def send_user(update, context):
    if update.effective_user.id in users_perm:
        context.bot.send_video(chat_id = update.effective_user.id, video = VIDEO_PROMO, 
        caption = "Grupo 👥 creado con el objetivo de q los usuarios 👤 de este canal puedan disfrutar de diversos 🤳 contenidos sin que se vean afectados 📈 sus paquete de datos móviles (total mente gratis)🚫💸\n\n● Juegos🕹\n● Series 🎥\n● Anime ⛩\n● Humor 😂",
        reply_markup = InlineKeyboardMarkup([[button_channel, button_group], [button_pxp1], [button_pxp2], [button_admin], [button_aportes1, button_aportes2]]))

def freack_promo(update, context):
    button1 = InlineKeyboardButton("📜Canal📜", url = "https://t.me/FreackChoiceS3")
    button2 = InlineKeyboardButton("📜Grupo de Chat📜", url = "https://t.me/FreackChoiceChatS3")
    button3 = InlineKeyboardButton("📜PxP 1📜", url = "https://t.me/EgoClamor")
    button4 = InlineKeyboardButton("📜PxP 2📜", url = "https://t.me/FaZe_Demon")
    context.bot.send_photo(chat_id = update.message.chat.id, photo = open("foto.jpg", "rb"),
    caption = "⚜️FreackChoiceS3⚜️\n\n“A veces, la mente recibe un golpe tan brutal que se esconde en la demencia. Puede parecer que eso no sea beneficioso, pero lo es. A veces, la realidad es solo dolor, y para huir de ese dolor, la mente tiene que abandonar la realidad.”\n\nAnime🖋\nVideojuegos🖋\nProgramas🖋\nMangas🖋\nNovelas ligeras🖋\nY más contenido Freak🖋\n\n🛡¿Que esperas para unirte? 🛡", 
    reply_markup = InlineKeyboardMarkup([
        [button1, button2],[button3, button4]
    ]))

updater = Updater(token = BOT_TOKEN, use_context = True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("p", send_user))
dp.add_handler(CommandHandler("pc", send_channel))
dp.add_handler(CommandHandler("asd", freack_promo))
dp.add_handler(MessageHandler(Filters.text, messages))
dp.add_handler(MessageHandler(Filters.photo, photo_to_channel))
dp.add_handler(MessageHandler(Filters.document, document_to_channel))

updater.start_polling()
print("Bot Iniciado!")
updater.idle()