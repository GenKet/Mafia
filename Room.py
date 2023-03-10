from uuid import uuid4
from telebot import TeleBot
from telebot.types import ReplyKeyboardRemove
from random import shuffle


class Room:
    def __init__(self, admin_chat, bot: TeleBot):
        self.bot = bot
        self.id = str(uuid4().int)[:5]
        self.admin = admin_chat
        self.users = []

    def get_link(self):
        return f'http://t.me/Test481234832948_Bot?start={self.id}'

    def add_user(self, user_chat, user_id):
        if user_chat not in self.users:
            self.users.append(user_chat)
            self.bot.send_message(self.admin, f'Пользователь {user_id} присоединился')
        else:
            self.bot.send_message(user_chat, 'Вы уже зашли в событие')

    def del_user(self, user_chat):
        if user_chat in self.users:
            self.users.remove(user_chat)
            self.bot.send_message(user_chat, 'Вы вышли из события', reply_markup=ReplyKeyboardRemove())
        else:
            self.bot.send_message(user_chat, 'Вы не вошли в событие')

    def begin_distribution(self, ids, call):
        if 12 >= len(self.users) >= 2:
            shuffle(cards)
            print(self.users)
            for n, i in enumerate(self.users):
                self.bot.send_message(i, 'Ваша карта:', reply_markup=ReplyKeyboardRemove())
                with open(f'cards/{cards[n]}.txt', 'r') as f:
                    self.bot.send_message(i, f.read())
            self.bot.send_message(self.admin, 'Карты розданы')
            self.bot.edit_message_reply_markup(ids, message_id=call.message.id, reply_markup=None)
        else:
            self.bot.send_message(self.admin,
                                  'Количество пользователей не больше 12 и не меньше 5! Удалите или добавьте кого-нибудь')

