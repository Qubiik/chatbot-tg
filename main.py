import telebot
import g4f

TOKEN = '6928486878:AAF4aslLmvrehZG6IoQBqimRZVOXrisLbNc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши мне что-нибудь.")

@bot.message_handler(func=lambda message: True)
def gpt(message):
  zapros = message.text
  response = g4f.ChatCompletion.create(
    model="gpt-4-0613",
    provider=g4f.Provider.GeekGpt,
    messages=[{"role": "user", "content": zapros}],
  )
  bot.reply_to(response)
bot.polling()