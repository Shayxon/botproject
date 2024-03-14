from .models import Question
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
import logging
import telebot
import random

TOKEN = '7135268912:AAFSJ8aj9el0frza0CP3UY2r6LdM-3_kL9E'

bot = telebot.TeleBot(TOKEN)

quiz = Question.objects.all()
answer = None

@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)
    
def question(message):
    global answer
    q = quiz[random.randint(0, 89)]
    bot.send_message(message.chat.id, q.question)    
    answer = q.answer
    
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'Welcome to math quiz bot!')
    question(message)

@bot.message_handler()
def send_message(message):
    global answer
    if message.text == answer:
        bot.send_message(message.chat.id, 'Your answer is correct!')
        question(message)
    else:
        bot.send_message(message.chat.id, 'Your answer is incorrect! Try again!')
