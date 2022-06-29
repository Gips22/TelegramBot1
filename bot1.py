import telebot  # библиотека позволяющая получать сообщения и выполнять обработку всех действий

"""
Тут мы обращаемся к классу  TeleBot, создаем ЭК с именем bot и передаем ему токен, который получаю в телеге через botfather, введя ему команды:
- /newbot
- затем ввожу название бота
botfather пишет мне, выдавая этот токен вот что: Use this token to access the HTTP API
"""
bot = telebot.TeleBot('5426658187:AAGAw5i0q7HTaImJnAtYHqvhDkyOxpyZkoA')


# Далее мы будем отслеживать команды введенные пользователем в боте
# Отслеживаем команду 'start'
@bot.message_handler(commands=['start'])
def start(message):  # тут параметр message это сообщение от пользователя
    # from_user.- получаем инфу о пользователе
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'

    """каждый раз теперь когда мы хотим взаимодействовать с ботом-мы будем обращаться к этой переменной
    тут мы обращаемся к метожду send_message класса TeleBot и передаем параметры. 1й параметр- в какой чат мы все отправляем
    2й параметр просто текст
    3 параметр -режим в котором мы отправляем текст. Можно обычный текст, а можно html- тогда можно прописывать теги
    """
    bot.send_message(message.chat.id, mess, parse_mode='html')


# Отслеживаем тип отправленного пользователем сообщения. Тут - формат фото.
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')


@bot.message_handler(commands=['website'])
def website(message):
    # types тут специальный объект через который мы можем создавать кнопки.
    # создаем стандартную кнопку через InlineKeyboardMarkup через создание ЭК этого же класса InlineKeyboardMarkup
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Посетить веб-сайт', url='https://google.com/'))
    bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    # Тут в resize_keyboard делаем адаптацию под устройства, а в row_width указываем сколько поместится кнопок в ряду.
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # Создаем кнопки
    website = telebot.types.KeyboardButton('Website')
    start = telebot.types.KeyboardButton('LetsGO')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Go to website', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        # chat.id -это в какой конкретно чат отправляем
        bot.send_message(message.chat.id, 'И тебе бонжур', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('/Users/andreynaletov/PycharmProjects/Bot1/pic.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Шо це робиш?', parse_mode='html')

# Запускаем бот на постоянное выполнение
bot.polling(none_stop=True)

