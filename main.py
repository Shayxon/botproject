import telebot
import requests


TOKEN = '7071070436:AAFXTvFBy4C8slS_5eMdnKOMY4ay9Y-OcBE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom men Ob hova botiman. Shahar nomini kiriting va shaharning hozirgi ob havosini bolib oling!")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city_name = message.text
    weather_data = fetch_weather(city_name)
    if weather_data:
        weather_message = format_weather_message(weather_data)
        bot.reply_to(message, weather_message)
    else:
        bot.reply_to(message, "Kechirasiz, Bu shaharning ob havosi haqida malumot topolmadim!")

def fetch_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID=9bc83a00a14767c91ab4b95ca218b6a9"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_weather_message(weather_data):
    city = weather_data['name']
    try:
        weather_description = get_weather_description(weather_data['weather'][0]['description'])
    except:
        weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp'] - 273.15
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    icon = get_weather_icon(weather_data['weather'][0]['icon'])
    message = f"Ob havo malumoti {city}: {icon} {weather_description}\nHarorat: {temperature:.2f}°C\nNamlik: {humidity}%\nShamol Tezligi: {wind_speed} m/s"
    return message

def get_weather_icon(icon_code):
    icons = {
        "01d": "☀️",
        "01n": "🌙",
        "02d": "⛅️",
        "02n": "🌙⛅️",
        "03d": "☁️",
        "03n": "☁️",
        "04d": "☁️",
        "04n": "☁️",
        "09d": "🌧",
        "09n": "🌧",
        "10d": "🌦",
        "10n": "🌧",
        "11d": "⛈",
        "11n": "⛈",
        "13d": "❄️",
        "13n": "❄️",
        "50d": "🌫",
        "50n": "🌫",
    }
    return icons.get(icon_code, "")

def get_weather_description(description):
    descriptions = {
        'overcast clouds': 'Bulutli',
        'broken clouds': 'Yarim Bulutli',
        'mist': 'Tumanli',
        'scattered clouds': 'Qisman Bulutli',
        'few clouds': 'Bulut Kam'
    }
    return descriptions[description]

bot.polling()
