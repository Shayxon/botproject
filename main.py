import telebot
import random as rn

TOKEN = '7071070436:AAFXTvFBy4C8slS_5eMdnKOMY4ay9Y-OcBE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Matematik oyin oynaymiz boshlash uchun 'savol' deb yozing")

javob = 0 

@bot.message_handler()
def reply_message(message):
    global javob
    if message.text == 'savol':
        a = rn.randint(1, 99)
        b = rn.randint(1, 99)
        savol = f"{a} + {b} = ?"
        bot.send_message(message.chat.id, savol)
        javob = a + b
    else:
        if message.text == str(javob):
            bot.reply_to(message, 'Javobingiz to\'gri')
            m = bot.send_message(message.chat.id, 'savol')
            reply_message(m)
        else:
            bot.reply_to(message, 'Javobingiz xato yana urinib koring!')

bot.polling()
