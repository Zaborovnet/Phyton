import telebot

TOKEN = "1193940212:AAGfjrf6eycvvizwgP7qHIc7O5E4lzUQjzo"
bot = telebot.TeleBot(TOKEN)
savedata={-1}
jopa={-1}
surname = '';
name = '';

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Видос на сегодня', 'Изменить')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global jopa;
    global savedata

    if message.text.lower() == 'видос на сегодня':
        bot.send_message(message.chat.id, name)
        bot.send_message(message.chat.id, 'Именно это нужно смотреть');
    elif message.text.lower() == 'изменить':
        bot.send_message(message.from_user.id, "Скинь url видоса?")
        bot.register_next_step_handler(message, opa)  # следующий шаг – функция get_name


def opa (message):  # получаем фамилию
        global name
        name = message.text
        bot.send_message(message.chat.id, 'Ваши данные учтены');

bot.polling()