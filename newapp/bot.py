import telebot

bot = telebot.TeleBot("5756119752:AAF_IeFYEFtuL-0_UZQsZalM5M5OfKwt-0g")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()