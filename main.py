import telebot
import sqlite3
from telebot import types
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '5402432597:AAF4ZX3fIFxHIP_XvQ1R6nK8byLQaRccN64'
ootzivi = ["Елена Ш" + "\n" + "⭐️⭐️⭐️⭐ 16.01.2020 ️"+"\n"+"Вкусно и достойно. Чисто, главное. Хорошее меню. Единственное, что удивило, это то, что нельзя взять ланч и поделиться с другим человеком им. Какая разница, деньги-то платим",
           "Наталья Р" + "\n" + "⭐️⭐⭐️⭐️⭐ 13.05.2022 ️"+"\n"+'Недавно мне довелось посетить в компании подруг сеть кофеен "Шоколадница", которая представлена в разных городах нашей страны. Я побывала там впервые, однако мои подруги - завсегдатаи, поскольку работают рядом и ходят сюда на бизнес-ланч. Отзывы у них о кофейне были хорошие. И мое мнение о "Шоколаднице" тоже оказалось положительным.',
           "Николай М" + "\n" + "⭐️️⭐️⭐⭐⭐ 21.03.2022 ️"+"\n"+"Когда мы едем в отпуск, всегда проезжаем через Москву. И всегда посещаем кофейню 'Шоколадница'. В ней очень вкусно готовят и горячее, и десерты с пирожными. Чаще всего мы кушаем там сладенькое и пьем кофе.",
           "Иван Н" + "\n" + "⭐️⭐️⭐️⭐ 24.12.2021 ️"+"\n"+"Результатом посещения этого кафе оказались довольны абсолютно все, цены в Шоколаднице не самые высокие, пришлось отдать чаевые за хороший сервис.С удовольствием посещу Шоколадницу в нашем городе, а в питерском филиале очень рекомендую посидеть отдохнуть с чашкой горячего кофе.Благодарю за внимание и желаю отличного настроения!",
           "Ирина К" + "\n" + "⭐️⭐️⭐⭐️⭐ 17.07.2022"+"\n"+ "В 'Шоколаднице' всегда есть авторские напитки, и довольно редкие виды чая и кофе, что мне нравится. Вчера я там поела на 850 рублей, но я считаю, что это даже не особо дорого, потому что качество пищи, которую там готовят - на высшем уровне, и там всегда вкусно."]

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
    bot.send_message(message.chat.id, "Это ID удалили из базы данных!")



# @bot.message_handler(commands = ['delete'])
# def remove(message):
#     connect = sqlite3.connect('uusery.db')
#     cursor = connect.cursor()

#     people_id = message.chat.id
#     cursor.execute(f"DELETE FROM choco WHERE id = {people_id}")
#     connect.commit()
#     bot.send_message(message.chat.id, "Бронь с этого ID удалили из базы данных!")


@bot.message_handler(commands = ['start'])
def start(message):


    bot.send_message(message.chat.id, "Здравстуйте,  " + message.from_user.first_name + '!' +' 🍰')
    all = types.InlineKeyboardMarkup(row_width=1)
    site = types.InlineKeyboardButton("Официальный сайт", url = "https://shoko.ru/")
    menu = types.InlineKeyboardButton("Меню", url = "https://shoko.ru/menu/")
    all.add(site, menu)

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
        time.add(types.KeyboardButton("10:00"),types.KeyboardButton("11:00"),types.KeyboardButton("12:00"),types.KeyboardButton("13:00"),types.KeyboardButton("14:00"),types.KeyboardButton("15:00"),types.KeyboardButton("16:00"),types.KeyboardButton("17:00"),types.KeyboardButton("18:00"), types.KeyboardButton("19:00"), types.KeyboardButton("20:00"))

        ass = bot.send_message(message.chat.id, "⏰" + "\n"+ "Выберете время", reply_markup=time)
        bot.register_next_step_handler(ass, asd)
    elif message.text ==  "Отзывы":
        yoy= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        yoy.add(types.KeyboardButton("Балдеж!"))
        count = 5
        page = 1
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=' '),
                   InlineKeyboardButton(text='>', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))

        oy= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        oy.add(types.KeyboardButton("На главную"))
        iu = bot.send_message(message.from_user.id, "Отзывы", reply_markup = oy)
        bot.send_message(message.chat.id,ootzivi[page-1], reply_markup = markup)
        bot.register_next_step_handler(iu,new_new)

    elif message.text== "Все адреса":
        ups=types.ReplyKeyboardMurkup(resize_keyboard=True, row_width=2)
        ups.add(types.KeyboardButton("На главную"))
        ay=bot.send_message(message.chat.id,"доделать",reply_markup=ups)
        bot.register_next_step_handler(ay,ups)

        # bot.register_next_step_handler(qwerty,new_new)
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    req = call.data.split('_')
    #Обработка кнопки - скрыть
    # if req[0] == 'unseen':
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    #Обработка кнопок - вперед и назад
    if 'pagination' in req[0]:
    #Расспарсим полученный JSON
        json_string = json.loads(req[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
            #Пересоздаем markup
        markup = InlineKeyboardMarkup()
        # markup.add(InlineKeyboardButton(ootzivi[page-1], callback_data='unseen'))
        #markup для первой страницы
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'>',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page + 1) + ",\"CountPage\":" + str(count) + "}"))
        #markup для второй страницы
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(
                                                page - 1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
        #markup для остальных страниц
        else:
            markup.add(InlineKeyboardButton(text=f'<', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                           InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                           InlineKeyboardButton(text=f'>', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))
        bot.edit_message_text(ootzivi[page-1],#f'Отзыв {page} из {count}',
                              reply_markup = markup, chat_id=call.message.chat.id, message_id=call.message.message_id)


def asd(message):
    timeses = str(message.text)
    info[0]=timeses
    chels = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    chels.add(types.KeyboardButton('1-2'), types.KeyboardButton('3-5'), types.KeyboardButton('6-8'))

    soob = bot.send_message(message.chat.id, "👪" + "\n"+ "Выберете кол-во персон", reply_markup=chels)
    bot.register_next_step_handler(soob, fit)
def fit(message):
    helihs = str(message.text)
    info[1] = helihs
    but = bot.send_message(message.chat.id, "☎️"  "\n"+ "Напишите номер телефона для бронирования без пробелов и каких либо знаков")
    bot.register_next_step_handler(but, number)
def number(message):
    for i in message.text:
        if (str(message.text)[0] == '8' and len(str(message.text)) == 11) or (str(message.text)[0] == '+' and str(message.text)[1] == '7' and len(str(message.text)) == 12):
            numbere = str(message.text)
            info[2]=numbere
            hood = bot.send_message(message.chat.id, "👻" "\n"+ "Напишите имя и фамилию человека, на чье имя будет зарегестрирована бронь")
            bot.register_next_step_handler(hood, bue)
            break
    else:
        asa = bot.send_message(message.chat.id, "Некорректный номер, попробуйте еще раз")
        bot.register_next_step_handler(asa, number)

def bue(message):
    name = str(message.text)
    info[3]=name
    knopka = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    knopka.add(types.KeyboardButton('Хочу исправить 👎'), types.KeyboardButton('Все верно 👍'))
    what = bot.send_message(message.chat.id, "Подтверждение брони:" + "\n"+"Столик на " + str(info[0]) + ' на '+ str(info[1])+ " персон " + "забронирован на номер " + str(info[2]) + " на имя " + str(info[3]),reply_markup=knopka)
    bot.register_next_step_handler(what, suuubd)

def suuubd(message):
    if message.text == "Хочу исправить 👎":
        time = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        time.add(types.KeyboardButton("12:00"), types.KeyboardButton("13:00"), types.KeyboardButton("14:00"), types.KeyboardButton("15:00"), types.KeyboardButton("16:00"),
                 types.KeyboardButton("17:00"), types.KeyboardButton("18:00"), types.KeyboardButton("19:00"), types.KeyboardButton("20:00"))
        ass = bot.send_message(message.chat.id, "Выберете время", reply_markup=time)
        bot.register_next_step_handler(ass, asd)
    else:
        fine = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        fine.add(types.KeyboardButton("Отлично!"))

        azaza = bot.send_message(message.chat.id, "Бронь подтверждена!", reply_markup = fine)
        bot.register_next_step_handler(azaza, woow)


def woow(message):
    if str(message.chat.id)=="1351828821":
        bot.send_message(message.chat.id, "Сержу вход запрещен!")
    else:
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
            sql = "INSERT INTO choco (id, name, time, count, phone) VALUES (?, ?, ?, ?, ?)"
            val = (str(user_id), info[3],info[0], info[1], info[2])
            cursor.execute(sql, val)
            connect.commit()
            oy= types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            oy.add(types.KeyboardButton("Замечтательно!"))
            lol =bot.send_message(message.chat.id, "Вбили в базу данных!", reply_markup=oy)
            bot.register_next_step_handler(lol,new_new)
        else:
            bot.send_message(message.chat.id, "На это имя уже существует бронь!")




# timestamp not null default current_timestamp
# delete from choco where added_at < now()-interval 15 second


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








# # @bot.message_handler()
# # def af(message):
# #     if message.text == "Photo":
# #         photo = open("i (1).jpg", 'rb')
# #         bot.send_photo(message.chat.id, photo)
# # @bot.message_handler(content_types=['photo'])
# # def dds(message):
# #     bot.send_message(message.chat.id, "Классное фото!")

bot.polling(none_stop = True)
