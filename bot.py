import conf
import telebot
from telebot.types import Message

bot = telebot.TeleBot(conf.BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())



bot.polling()