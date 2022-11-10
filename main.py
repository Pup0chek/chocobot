import telebot
import sqlite3
from telebot import types

token = '5402432597:AAF4ZX3fIFxHIP_XvQ1R6nK8byLQaRccN64'

info = ["","","",""]
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['add'])
def add(message):
    connect = sqlite3.connect('uusery.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(id INTEGER)""")
    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", (user_id))
        connect.commit()
        bot.send_message(message.chat.id, "Вбили в базу данных!")
    else:
        bot.send_message(message.chat.id, "Такое ID уже есть в базе данных!!")








@bot.message_handler(commands = ['delete'])
def delete(message):
    connect = sqlite3.connect('uusery.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()
    bot.send_message(message.chat.id, "Это ID удалили из быза данных!")


@bot.message_handler(commands = ['start'])
def start(message):


    bot.send_message(message.chat.id, "Здравстуйте,  " + message.from_user.first_name + '!')
    all = types.InlineKeyboardMarkup(row_width=1)
    site = types.InlineKeyboardButton("Официальный сайт", url = "https://shoko.ru/")
    menu = types.InlineKeyboardButton("Меню", url = "https://shoko.ru/menu/")
    cringe = types. InlineKeyboardButton("Кринж мастер", url="https://vk.com/shenjashuk")
    all.add(site, menu, cringe)

    rmk = types.ReplyKeyboardMarkup(resize_keyboard= True)
    rmk.add(types.KeyboardButton('Еще'))
    bot.send_message(message.chat.id, "Выберете интересующий Вас вопрос:", reply_markup=all)
    msg = bot.send_message(message.chat.id, "Если интересующего Вас вопроса не оказалось в списке, нажмите на кнопку ЕЩЕ", reply_markup=rmk)
    bot.register_next_step_handler(msg, new_new)

def new_new(message):
    rock = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    rock.add(types.KeyboardButton("Ваш телефон"),types.KeyboardButton("Забронировать столик"), types.KeyboardButton("Отзывы"),types.KeyboardButton("Все адреса"))

    mess = bot.send_message(message.chat.id, "Выберете вопрос", reply_markup=rock)
    bot.register_next_step_handler(mess, aaaa)

def aaaa(message):
    if message.text == "Ваш телефон":
        dada = bot.send_message(message.chat.id, "+7 915 107-39-80")
        ret = types.ReplyKeyboardMarkup(resize_keyboard= True)
        ret.add(types.KeyboardButton("Еще"))
        bot.send_message(message.chat.id, "Если остались вопросы, нажмите на кнопку ЕЩЕ", reply_markup=ret)
        bot.register_next_step_handler(dada, new_new)
    elif message.text == "Забронировать столик":
        time = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        time.add(types.KeyboardButton("12:00"), types.KeyboardButton("13:00"), types.KeyboardButton("14:00"), types.KeyboardButton("15:00"), types.KeyboardButton("16:00"),
                 types.KeyboardButton("17:00"), types.KeyboardButton("18:00"), types.KeyboardButton("19:00"), types.KeyboardButton("20:00"), types.KeyboardButton("21:00"))
        ass = bot.send_message(message.chat.id, "Выберете время", reply_markup=time)
        bot.register_next_step_handler(ass, asd)
    elif message.text ==  "Отзывы":
        bot.send_message(message.chat.id, "Ознакомиться с отзывами вы сможете, перейдя по ссылке")

def asd(message):
    timeses = str(message.text)
    info[0]=timeses
    chels = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    chels.add(types.KeyboardButton('1-2'), types.KeyboardButton('3-5'), types.KeyboardButton('6-8'))

    soob = bot.send_message(message.chat.id, 'Выберете кол-во персон', reply_markup=chels)
    bot.register_next_step_handler(soob, fit)
def fit(message):
    helihs = str(message.text)
    info[1] = helihs
    but = bot.send_message(message.chat.id, "Напишите номер телефона для бронирования без пробелов и каких либо знаков")
    bot.register_next_step_handler(but, number)
def number(message):
    for i in message.text:
        if (str(message.text)[0] == '8' and len(str(message.text)) == 11) or (str(message.text)[0] == '+' and str(message.text)[1] == '7' and len(str(message.text)) == 12):
            numbere = str(message.text)
            info[2]=numbere
            hood = bot.send_message(message.chat.id, "Напишите имя и фамилию человека, на чье имя будет зарегестрирована бронь")
            bot.register_next_step_handler(hood, bue)
            break
    else:
        asa = bot.send_message(message.chat.id, "Некорректный номер, попробуйте еще раз")
        bot.register_next_step_handler(asa, number)

def bue(message):
    name = str(message.text)
    info[3]=name
    knopka = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    knopka.add(types.KeyboardButton('Хочу исправить'), types.KeyboardButton('Все верно'))
    what = bot.send_message(message.chat.id, "Подтверждение брони:" + "\n"+"Столик на " + str(info[0]) + ' на '+ str(info[1])+ " персон " + "забронирован на номер " + str(info[2]) + " на имя " + str(info[3]),reply_markup=knopka)
    bot.register_next_step_handler(what, suuubd)

def suuubd(message):
    if message.text == "Хочу исправить":
        time = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        time.add(types.KeyboardButton("12:00"), types.KeyboardButton("13:00"), types.KeyboardButton("14:00"), types.KeyboardButton("15:00"), types.KeyboardButton("16:00"),
                 types.KeyboardButton("17:00"), types.KeyboardButton("18:00"), types.KeyboardButton("19:00"), types.KeyboardButton("20:00"), types.KeyboardButton("21:00"))
        ass = bot.send_message(message.chat.id, "Выберете время", reply_markup=time)
        bot.register_next_step_handler(ass, asd)
    else:
        fine = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        fine.add(types.KeyboardButton("Отлично!"))

        azaza = bot.send_message(message.chat.id, "Бронь подтверждена!", reply_markup = fine)
        bot.register_next_step_handler(azaza, woow)


def woow(message):
    connect = sqlite3.connect("uusery.db")
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS choco(
        id INTEGER,
        name VARCHAR,
        time VARCHAR,
        count VARCHAR,
        phone VARCHAR
    )""")

    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM choco WHERE id = {people_id}")
    data = cursor.fetchone()
    if data == None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO choco VALUES(?, ?, ?, ?, ?);", (user_id, info[3],info[0], info[1], info[2]),)
        connect.commit()
        bot.send_message(message.chat.id, "Вбили в базу данных!")
    else:
        bot.send_message(message.chat.id, "На это имя уже существует бронь!")

# import sqlite3
# db = sqlite3.connect('uusery.db')
# sql = db.cursor()

# sql.execute("""CREATE TABLE IF NOT EXISTS users(
#     name TEXT,
#     phone TEXT,
#     time TEXT,
#     count TEXT
# )""")
# named = str(info[3])
# phoned = str(info[2])
# timed = str(info[0])
# countd = str(info[1])
# db.commit()
# def prove(message):

#     sql = db.cursor()

#     sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (named, phoned, timed, countd))
#     db.commit()
#     bot.send_message(message.chat.id, "Зарегестрировано!")
#     info.clear()

# @bot.message_handler(commands = ['wow'])
# def wow(message):
#     for value in sql.execute("SELECT * FROM users"):
#         bot.send_message(chat.message.id, value)





bot.polling(none_stop = True)
