from aiogram import types
# Клавиши


# Start
def implementer_inlinkeyboard():
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_1 = types.InlineKeyboardButton('Исполнитель', callback_data='button_1')
    button_2 = types.InlineKeyboardButton('Заказчик', callback_data='button_2')
    markup.add(button_1, button_2)
    return markup
# Сообщение которое отправляется исполнителю первое Клавиатура для команды Исполнитель
def implementer_inlinkeyboard_1():
    markup = types.InlineKeyboardMarkup(resize_keyboard = True, selective = True)
    button_3 = types.InlineKeyboardButton('Ваши работы', callback_data='implementer_button_3')
    button_4 = types.InlineKeyboardButton('Найти работу', callback_data='implementer_button_4')
    #button_5 = types.InlineKeyboardButton('Личный профиль', callback_data='implementer_button_5')
    button_6 = types.InlineKeyboardButton('Связь с админом', callback_data='implementer_button_6')
    markup.row(button_3, button_4) # Можно ли создать button_1 или он будет вызываться всегда
    markup.row(button_6)
    return markup
for i in range(1,100):
    print(+11)

# Клавиатура для пункта Ваши работы
def inlinekeyboard_3():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_7 = types.InlineKeyboardButton('Информация о заказе', callback_data='button_7')
    button_8 = types.InlineKeyboardButton('Ссылка на чат', callback_data='button_8')
    markup.add(button_7, button_8)
    return markup

# Клавиатура для пункта Найти работу
def inlinekeyboard_4():
    markup = types.InlineKeyboardMarkup(resize_keyboard=True, selective=True)
    button_9 = types.InlineKeyboardButton('Программист', callback_data='implementer_button_9')
    button_10 = types.InlineKeyboardButton('Юрист', callback_data='implementer_button_10')
    button_11 = types.InlineKeyboardButton('Экономист', callback_data='implementer_button_11')
    button_12 = types.InlineKeyboardButton('Естественник', callback_data='implementer_button_12')
    button_13 = types.InlineKeyboardButton('Гуманитарий', callback_data='implementer_button_13')
    button_14 = types.InlineKeyboardButton('Технарь', callback_data='implementer_button_14')
    #button_15 = types.InlineKeyboardButton('Список работ', callback_data='button_15')
    markup.row(button_9, button_10, button_11)
    markup.row(button_12, button_13)
    markup.row(button_14)
    return markup
