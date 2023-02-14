
import telebot
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from Room import Room

bot = telebot.TeleBot('5569661722:AAHRgLf9iGOHRLgp9djaMBTtdQrPC_1b1yU')
rooms = []


def extract_room_id(text):
    return text.split()[1] if len(text.split()) > 1 else None


@bot.message_handler(commands=['start'])
def choose_role(message: Message):
    room_id = extract_room_id(message.text)

    if room_id:
        for i in rooms:
            if i.id == room_id:
                markup = InlineKeyboardMarkup()
                outbtn = InlineKeyboardButton('Выйти', callback_data=f'out_{room_id}')
                markup.add(outbtn)
                i.add_user(message.chat.id, message.from_user.username)
                bot.send_message(message.chat.id, f'Здравствуйте, вы добавлены в событие {add}', reply_markup=markup)
    else:
        createbtn = InlineKeyboardButton('Создать событие', callback_data='create')
        searchbtn = InlineKeyboardButton('Поиск по событиям', callback_data='search')
        markup = InlineKeyboardMarkup().add(createbtn,searchbtn)
        bot.send_message(message.chat.id, 'Здравствуйте, вы зашли как администратор', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call: CallbackQuery):
    ids = call.message.chat.id
    bot.answer_callback_query(call.id)
    match call.data.split('_')[0]:
        case 'create':
            room = Room(ids, bot)
            rooms.append(room)
            delbtn = InlineKeyboardButton('Удалить событие', callback_data=f'delete_{room.id}')
            photobtn = InlineKeyboardButton('Добавить фото события', callback_data=f'photo_{room.id}')
            addnamebtn = InlineKeyboardButton('Добавить название события', callback_data=f'name_{room.id}')
            adddisbtn = InlineKeyboardButton('Добавить описание события', callback_data=f'dis_{room.id}')
            adddatebtn = InlineKeyboardButton('Добавить дату события и время начало в формате(чч.мм.гг (время начало))', callback_data=f'date_{room.id}')
            endbtn = InlineKeyboardButton('Добавить окончание события', callback_data=f'end_{room.id}')
            markup = InlineKeyboardMarkup().add(delbtn,photobtn,addnamebtn,adddisbtn,adddatebtn,endbtn)
            bot.send_message(ids, f'Комната создана!\nСсылка на комнату:\n{room.get_link()}',
                             reply_markup=markup)
        case 'start':
            idr = call.data.split('_')[1]
            for i in rooms:
                if i.id == idr:
                    i.begin_distribution(ids, call)
                    break
        case 'delete':
            idr = call.data.split('_')[1]
            for i in rooms:
                if i.id == idr:
                    rooms.remove(i)
                    break
            bot.send_message(ids, f'Комната удалена')
        case 'out':
            idr = call.data.split('_')[1]
            for i in rooms:
                if i.id == idr:
                    i.del_user(ids)
        case 'name':
            idr = call.data.split('_')[1]
            for i in rooms:
                if i.id == idr:
                    bot.send_message(ids, f'Введи название события')

                    bot.send_message(ids, name)
                    break



bot.infinity_polling()
