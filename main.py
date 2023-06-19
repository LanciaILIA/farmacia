import telebot
import traceback
import farmacia
from config import TOKEN, name, email_lor, email_pent, email_ind


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['лекарство'])
def values(message: telebot.types.Message):
    text = 'Выберите препарат:'
    for i in name.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def choice(message: telebot.types.Message):
    medication_ = message.text
    medication = medication_.lower()

    try:
        if medication == 'пенталгин':
            email = email_pent
        if medication == 'лориста':
            email = email_lor
        if medication == 'индапамид':
            email = email_ind

        answer_vita = farmacia.vita(email)
        answer_mosk = farmacia.mosk(email)
        answer_ru = farmacia.ru(email)

    except UnboundLocalError:
        bot.reply_to(message, f"препарат не найден")

    else:
        bot.reply_to(message, answer_vita)
        bot.reply_to(message, answer_mosk)
        bot.reply_to(message, answer_ru)


bot.polling()
