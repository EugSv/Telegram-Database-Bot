import telebot
from TG_database import save_data, read_data, delete_data

TOKEN = '###'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для работы с базой данных.\n"
                          "Доступные команды:\n"
                          "/add Имя Фамилия Возраст - Добавить запись\n"
                          "/read - Показать все записи\n"
                          "/delete ID - Удалить запись по ID")

@bot.message_handler(commands=['add'])
def add_data(message):
    try:
        name, surname, age = message.text.split()
        save_data(name, surname, int(age))
        bot.reply_to(message, f"Добавлена запись: {name} {surname}, {age} лет.")
    except ValueError:
        bot.reply_to(message, "Ошибка! Используйте формат: /add Имя Фамилия Возраст")

@bot.message_handler(commands=['read'])
def read_all_data(message):
    records = read_data()
    if records:
        bot.reply_to(message, "\n".join(records))
    else:
        bot.reply_to(message, "База данных пуста.")

@bot.message_handler(commands=['delete'])
def delete_record(message):
    try:
        _, record_id = message.text.split()
        if delete_data(int(record_id)):
            bot.reply_to(message, f"Запись с ID {record_id} удалена.")
        else:
            bot.reply_to(message, "Ошибка! Запись с таким ID не найдена.")
    except ValueError:
        bot.reply_to(message, "Ошибка! Используйте формат: /delete ID")

bot.polling()