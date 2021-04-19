from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def inlinkeyboard():
    markup = InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_1 = InlineKeyboardButton('Исполнитель', callback_data='button_1')
    button_2 = InlineKeyboardButton('Заказчик', callback_data='button_2')
    button_admin = InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.add(button_1, button_2, button_admin)
    return markup

def customer_keyboard1():    #########     клавы для предметов
    markup = InlineKeyboardMarkup(resize_keyboard = False, selective = True)
    button_3 = InlineKeyboardButton('Гуманитарий', callback_data='customer_button_1')
    button_4 = InlineKeyboardButton('Программист', callback_data='customer_button_2')
    button_5 = InlineKeyboardButton('Юрист', callback_data='customer_button_3')
    button_6 = InlineKeyboardButton('Технарь', callback_data='customer_button_4')
    button_7 = InlineKeyboardButton('Естественник', callback_data='customer_button_5')
    button_8 = InlineKeyboardButton('Экономист', callback_data='customer_button_6')
    button_9 = InlineKeyboardButton('⬅ Назад', callback_data='back1')
    button_10 = InlineKeyboardButton('Связь с админом', callback_data='admin', url='https://t.me/i_Tele_2')
    button_admin = InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.add(button_3, button_4, button_5, button_6, button_7, button_8)
    markup.row(button_9)
    markup.row(button_admin)
    return markup


def customer_keyboard2():
    markup = InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_customer_1 = InlineKeyboardButton('Как можно скорее', callback_data='customer_button_7')
    button_customer_2 = InlineKeyboardButton('1-2 дня', callback_data='customer_button_8')
    button_customer_3 = InlineKeyboardButton('2-4 дня', callback_data='customer_button_9')
    button_customer_4 = InlineKeyboardButton('в течение 7 дней', callback_data='customer_button_10')
    button_customer_5 = InlineKeyboardButton('ввести свой срок исполнения', callback_data='customer_button_11')
    button_customer_6 = InlineKeyboardButton('⬅ Назад', callback_data='back2')
    button_admin = InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.row(button_customer_1)
    markup.add(button_customer_2, button_customer_3)
    markup.row(button_customer_4)
    markup.row(button_customer_5)
    markup.row(button_customer_6)
    markup.row(button_admin)
    return markup

def customer_keyboard3():
    markup = InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_customer_1 = InlineKeyboardButton('100руб', callback_data='customer_button_12')
    button_customer_2 = InlineKeyboardButton('200руб', callback_data='customer_button_13')
    button_customer_3 = InlineKeyboardButton('300руб', callback_data='customer_button_14')
    button_customer_4 = InlineKeyboardButton('400руб', callback_data='customer_button_15')
    button_customer_5 = InlineKeyboardButton('500руб', callback_data='customer_button_16')
    button_customer_6 = InlineKeyboardButton('600руб', callback_data='customer_button_17')
    button_customer_7 = InlineKeyboardButton('700руб', callback_data='customer_button_18')
    button_customer_8 = InlineKeyboardButton('800руб', callback_data='customer_button_19')
    button_customer_9 = InlineKeyboardButton('900руб', callback_data='customer_button_20')
    button_customer_10 = InlineKeyboardButton('1000руб', callback_data='customer_button_21')
    button_customer_12 = InlineKeyboardButton('Ввести свою цену: ', callback_data='customer_button_22')
    button_customer_11 = InlineKeyboardButton('⬅ Назад', callback_data='back3')
    button_admin = InlineKeyboardButton('Связь с админом', callback_data='button_6', url='https://t.me/i_Tele_2')
    markup.add(button_customer_1,button_customer_2,button_customer_3,button_customer_4,
               button_customer_5, button_customer_6, button_customer_7, button_customer_8,
               button_customer_9, button_customer_10)
    markup.row(button_customer_12)
    markup.row(button_customer_11)
    markup.row(button_admin)
    return markup

def customer_keyboard_yes_no():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = KeyboardButton('Да')
    button2 = KeyboardButton('Нет')
    markup.add(button1,button2)
    return markup










