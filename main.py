import telebot
import sqlite3
from telebot import types

token = '5402432597:AAF4ZX3fIFxHIP_XvQ1R6nK8byLQaRccN64'

info = []
bot = telebot.TeleBot(token)
tochki = ['ЛЕНИНСКАЯ СЛОБОДА УЛ., Д. 26', "ДМИТРИЯ УЛЬЯНОВА УЛ., Д. 24", "БОЛЬШАЯ ЧЕРЕМУШКИНСКАЯ УЛ., Д.1, ТЦ РИО","МИРА ПР-КТ, Д. 112"]

@bot.message_handler(commands = ['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        Имя INTEGER
    )""")

    connect.commit()


    id_user = [message.chat.id]
    cursor.execute("INSERT INTO login_id VALUES(?);", id_user)
    connect.commit()

    bot.send_message(message.chat.id, "Здравстуйте,  " + message.from_user.first_name + '!')
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
        time.add(types.KeyboardButton("12:00"), types.KeyboardButton("13:00"), types.KeyboardButton("14:00"), types.KeyboardButton("15:00"), types.KeyboardButton("16:00"),
                 types.KeyboardButton("17:00"), types.KeyboardButton("18:00"), types.KeyboardButton("19:00"), types.KeyboardButton("20:00"), types.KeyboardButton("21:00"))
        ass = bot.send_message(message.chat.id, "Выберете время", reply_markup=time)
        bot.register_next_step_handler(ass, asd)

def asd(message):
    timeses = str(message.text)
    info.append(timeses)
    chels = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
    chels.add(types.KeyboardButton('1-2'), types.KeyboardButton('3-5'), types.KeyboardButton('6-8'))

    soob = bot.send_message(message.chat.id, 'Выберете кол-во персон', reply_markup=chels)
    bot.register_next_step_handler(soob, fit)
def fit(message):
    helihs = str(message.text)
    info.append(helihs)
    but = bot.send_message(message.chat.id, "Напишите номер телефона для бронирования без пробелов и каких либо знаков")
    bot.register_next_step_handler(but, number)
def number(message):
    for i in message.text:
        if (str(message.text)[0] == '8' and len(str(message.text)) == 11) or (str(message.text)[0] == '+' and str(message.text)[1] == '7' and len(str(message.text)) == 12):
            numbere = str(message.text)
            info.append(numbere)
            hood = bot.send_message(message.chat.id, "Напишите имя и фамилию человека, на чье имя будет зарегестрирована бронь")
            bot.register_next_step_handler(hood, bue)
            break
    else:
        asa = bot.send_message(message.chat.id, "Некорректный номер, попробуйте еще раз")
        bot.register_next_step_handler(asa, number)

def bue(message):
    name = str(message.text)
    info.append(name)
    bot.send_message(message.chat.id, "Подтверждение брони:" + "\n"+"Столик на " + str(info[0]) + ' на '+ str(info[1])+ " персон " + "забронирован на номер " + str(info[2]) + " на имя " + str(info[3]))
    more = types.ReplyKeyboardMarkup(resize_keyboard= True)
    more.add(types.KeyboardButton("Еще"))
    end = bot.send_message(message.chat.id, "Если остались вопросы, выберете интересующию тему, нажав на кнопку ЕЩЕ", reply_markup=more)
    bot.register_next_step_handler(end,new_new)
# @bot.message_handler(commands=['application'])
# def application(message):
#     rmk = types.ReplyKeyboardMarkup()
#     rmk.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
#
#     msg = bot.send_message(message.chat.id, 'Желаете подать заявку?', reply_markup = rmk)
#     bot.register_next_step_handler(msg, user_ans)

# def user_ans(message):
#     if message.text == "Да":
#         msg = bot.send_message(message.chat.id, 'Впишите ваши данные')
#         bot.register_next_step_handler(msg, user_reg)
#     elif message.text == "Нет":
#         bot.send_message(message.chat.id, 'Ok')
#     else:
#         bot.send_message(message.chat.id, 'Надо ответить на вопрос!')
#
# def user_reg(message):
#     bot.send_message(message.chat.id, f"your data:{message.text}")

@bot.message_handler(content_types= ['text'])
def get_text(message):
    if message.text == "еще" or message.text == "Еще" or message.text == "ЕЩЕ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        phone = types.KeyboardButton("Ваш телефон")
        all_cafe = types.KeyboardButton("Все адреса")
        table = types.KeyboardButton("Забронировать столик")
        markup.add(phone, all_cafe, table)
        bot.send_message(message.chat.id, "Нажмите интересующую кнопку", reply_markup=markup)
    elif message.text == "Все адреса":
        beggin = "Наши точки:"
        text = beggin.upper() + "\n"
        for i in tochki:
            text = text +'-' + i + "\n"
        bot.send_message(message.chat.id, text)
    elif message.text == "Ваш телефон":
        bot.send_message(message.chat.id, "+7 915-107-39-80")
    elif message.text == "Забронировать столик":
        alles = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        moskow = types.KeyboardButton("Москва")
        SPB = types.KeyboardButton("Санкт Петербург")
        red = types.KeyboardButton("Краснодар")
        ram = types.KeyboardButton("Раменское")
        alles.add(moskow, SPB, ram)
        bot.send_message(message.chat.id, "Выберете город", reply_markup=alles)
    elif message.text == "Москва":
        ol = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        awto = types.KeyboardButton("Автозаводская")
        akadem = types.KeyboardButton("Академическая")
        alexe = types.KeyboardButton("Алексеевская")
        alt = types.KeyboardButton("Алтуфьево")
        ann = types.KeyboardButton("Аннино")
        arb = types.KeyboardButton("Арбатская")
        ol.add(awto, akadem, alexe, alt, ann, arb)
        bot.send_message(message.chat.id, "Выберете метро", reply_markup=ol)
    elif message.text == "Раменское":
        oil = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        ram = types.KeyboardButton("Красноармейская ул,. 13А")
        oil.add(ram)
        bot.send_message(message.chat.id, "Выберете улицу", reply_markup=oil)
    elif message.text == "Красноармейская ул,. 13А":
        table = types.ReplyKeyboardMarkup(resize_keyboard= True, row_width=2)
        one = types.KeyboardButton("1-2")
        three = types.KeyboardButton("3-4")
        five = types.KeyboardButton("5-7")
        table.add(one, three, five)
        bot.send_message(message.chat.id, "Укажите количество гостей", reply_markup= table)
    elif message.text == "1-2" or message.text == "3-4" or message.text == "5-7":
        bot.send_message(message.chat.id, "Укажите пожалуйста ФИ человека, на имя которого будет забронирован столик и его номер телефона")
    else:
        bot.send_message(message.chat.id, "Ваш заказ обработан!")
        bot.send_message(message.chat.id, "Менеджер скоро свяжется с вами")


# # @bot.message_handler()
# # def af(message):
# #     if message.text == "Photo":
# #         photo = open("i (1).jpg", 'rb')
# #         bot.send_photo(message.chat.id, photo)
# # @bot.message_handler(content_types=['photo'])
# # def dds(message):
# #     bot.send_message(message.chat.id, "Классное фото!")

bot.polling(none_stop = True)
