import telebot
import random
TOKEN = open(".env").readline()


bot = telebot.TeleBot(TOKEN)
rnum = 0
cnt = 0
@bot.message_handler(commands = ['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Guess a number from 1 to 100!")
    global rnum
    rnum = random.randint(1, 100)
    #bot.send_message(chat_id, f"Number is {rnum}")

@bot.message_handler(content_types = ['text'])
def message_handler(message):
    chat_id = message.chat.id
    text = message.text.strip()
    if text.isdigit():
        global rnum
        num = int(text)
        global cnt
        cnt += 1
        if 1 <= num and num <= 100:
            if num == rnum:
                bot.send_message(chat_id, f"This is the correct number.\nIt took {cnt} tries.\n/start to restart the game.")
            elif num < rnum:
                bot.send_message(chat_id, "The number is higher.")
            elif num > rnum:
                bot.send_message(chat_id, "The number is lower.")
                
        else:
            bot.send_message(chat_id, "This number is not from 1 to 100.")
    else:
        bot.send_message(chat_id, "This is not a number.")
bot.polling()
