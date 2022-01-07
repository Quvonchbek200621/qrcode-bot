from telegram.ext import Updater,ConversationHandler,CommandHandler,MessageHandler,Filters

import qrcode  # bu joyga qrcod kutubxonasi dasturga yuklanadi





wer=[

def start(update,context):

    update.message.reply_html(

        '<b>Assalomu alaykum  {}</b>'.format(update.message.from_user.first_name)+"\nQR kod uchun <b>TEXT</b> yokiy <b>URL</b> ma'lumot kiriting.")

    aa=update.message.text

    wer.append(aa)

    return 1

def ism(update,context):

    ab = update.message.text

    if ab=="balans":

        f=open("balans.txt","r")

        aaa=f.readline()

        context.bot.sendMessage(update.effective_chat.id,text=("Foydalanildi:  "+aaa))

        f.close()

    else:

        f = open("balans.txt", "r")

        aa=f.readline()

        f.close()

        aa1=int(aa)

        aa1=aa1+1

        ff=open("balans.txt","w")

        ff.write(str(aa1))

        ff.close()

        qr = qrcode.QRCode(

            version=1,

            error_correction=qrcode.constants.ERROR_CORRECT_L,

            box_size=10

        )

        qr.add_data(ab)

        qr.make(fit=True)

        # quyida yaratilayotgan qrcod rangi va orqa fon rangi kiritiladi

        img = qr.make_image(fill_color="black", back_color="white")

        # hujjat homi fayl kengaytmasi bilan birga kiritiladi

        img.save("@qrcode_qr_kodbot.jpg", "JPEG")

        update.message.reply_text("QR kod tayyor bo'ldi")

        context.bot.sendPhoto(update.effective_chat.id,photo=open('@qrcode_qr_kodbot.jpg',"rb"))

updater=Updater(' token ',use_context=True)

dp=updater.dispatcher

chandler=ConversationHandler(

    entry_points=[CommandHandler('start',start)],

    states={

        1:[CommandHandler("start",start),MessageHandler(Filters.text,ism)],

    },

    fallbacks=[MessageHandler(Filters.text,start)]

)

dp.add_handler(chandler)

updater.start_polling()

updater.idle()

