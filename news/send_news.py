import telebot

TOKEN = '7135268912:AAFSJ8aj9el0frza0CP3UY2r6LdM-3_kL9E'

bot = telebot.TeleBot(TOKEN)


def send_news(title, body, users):
    for user in users:
        bot.send_message(int(user.tel_user_id), f'{title}\n {body}')