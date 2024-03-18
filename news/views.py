from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import logging
import telebot
from .models import Email, Users

TOKEN = '7135268912:AAFSJ8aj9el0frza0CP3UY2r6LdM-3_kL9E'

bot = telebot.TeleBot(TOKEN)
email = True

@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)   
    
@bot.message_handler(commands=['start'])
def send_message(message):
    global email
    bot.send_message(message.chat.id, 'Welcome to news bot!')
    bot.send_message(message.chat.id, 'Please enter your email!')
    email = True

@bot.message_handler()
def ask_email(message):
        global email
        if email:
            if message.text not in Email.objects.values_list('email', flat=True):
                mail = Email(email=message.text)
                mail.save()
                if str(message.from_user.id) not in Users.objects.values_list('tel_user_id', flat=True):
                    user = Users(tel_user_id=message.from_user.id)
                    user.save()
                bot.send_message(message.chat.id, 'Email is registered!')
                email = False
            else:            
                bot.send_message(message.chat.id, 'Email already exists enter another email address!')
        else:
            bot.send_message(message.chat.id, 'You cannot send message!')

def send_news(title, body):
    bot.send_message(f'{title}\n {body}')         