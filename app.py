from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import state
from data.config import my_token
from Utils.set_bot_commands import set_default_commands
from keyboard.inlinekeyboard.implementer import *
from keyboard.inlinekeyboard.customer import customer_keyboard1,\
    customer_keyboard2, customer_keyboard3, inlinkeyboard, customer_keyboard_yes_no
from time import sleep
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from DataBase import add_to_database_customer, add_to_database_implementer, get_orders_by_price
import datetime
import testBot

class Customer(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()

class Implementer(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()

bot = Bot(token=my_token)
dp = Dispatcher(bot, storage=MemoryStorage())


# @dp.message_handler(content_types=['text'])
# async def send_text(message, s,):
#     global first_id
#     global second_id
#     first_id = 719274325
#     second_id = 484050440
#     @dp.message_handler(content_types=['text'])
#     async def send_text(message):
#         answer = message.text
#         if int(message.from_user.id) == int(first_id):
#             await bot.send_message(second_id, answer)
#         elif int(message.from_user.id) == int(second_id):
#             await bot.send_message(first_id, answer)


global a, b

'''
'''
async def on_startup(dp):
    await set_default_commands(dp)

# @dp.callback_query_handlers(funk = lambda c: c.data and c.data.startswith('button_1'))
@dp.callback_query_handler(lambda c: c.data == 'button_1')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Меню для исполнителя:', reply_markup=implementer_inlinkeyboard_1())
    add_to_database_implementer(callback_query.from_user.username, callback_query.from_user.id)

@dp.callback_query_handler(lambda c: c.data == 'button_2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите направление :', reply_markup=customer_keyboard1())

@dp.callback_query_handler(lambda c: c.data == 'back1')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись в главное меню\n'
                                                        'Выберите направление :', reply_markup=inlinkeyboard())

"""
#########  снизу идет поиск заказов для исполнителя
"""
@dp.callback_query_handler(lambda c: c.data == 'implementer_button_4')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите направление :', reply_markup=inlinekeyboard_4())

@dp.callback_query_handler(lambda c: c.data == 'implementer_button_9')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Программист'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()

@dp.callback_query_handler(lambda c: c.data == 'implementer_button_10')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Юрист'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()

@dp.callback_query_handler(lambda c: c.data == 'implementer_button_11')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Экономист'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()


@dp.callback_query_handler(lambda c: c.data == 'implementer_button_12')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Естественник'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()

@dp.callback_query_handler(lambda c: c.data == 'implementer_button_13')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Гуманитарий'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()

@dp.callback_query_handler(lambda c: c.data == 'implementer_button_14')
async def process_for_button_1(callback_query: types.CallbackQuery):
    global imp_sub
    imp_sub = 'Технарь'
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'От какой суммы рассматриваете заказ? ')
    await Implementer.question1.set()

@dp.message_handler(state=Implementer.question1)  ### первое состяоние для исполнителя (цена от)
async def send_text(message : types.message, state:FSMContext):
    global search_price
    search_price = message.text
    answer = get_orders_by_price(imp_sub, search_price)
    await message.answer(answer[0])
    await message.answer('Выберите номер заказа: ')
    await Implementer.question2.set()
@dp.message_handler(state = Implementer.question2) ### второе состояние для исполнителя (выбираем заказ)
async def send_text1(message : types.message, state:FSMContext):
    number = message.text
    await state.update_data(answer1=number)
    answer = get_orders_by_price(imp_sub, search_price)
    if len(answer[1]) < int(number) or int(number) < 0:
        await message.answer('заказов всего {}, вы ввели неправильную цифру'.format(len(answer[1])))
        await message.answer('Введите ещё раз цифру')
    else:
        await message.answer('вы выбрали заказ под номером {}'.format(number))
        await Implementer.question3.set()
        await message.answer('вы находитесь в переписке с заказчиком')

@dp.message_handler(state = Implementer.question3)
async def send_text(message : types.message, state:FSMContext):
    text = message.text
    answer = get_orders_by_price(imp_sub, search_price)[1]
    await state.update_data(answer2 = answer)
    data = await state.get_data()
    data = data.get('answer1')
    # if int(message.from_user.id) == int(message.from_user.id):
    #     await bot.send_message(int(answer[int(data)-1]), text)
    # elif int(message.from_user.id) == int(answer[int(data)-1]):
    #     await bot.send_message(message.from_user.id, text)
    dp.stop_polling()
    sleep(2)
    testBot.main(int(answer[int(data)-1]), message.from_user.id)


"""
######### сверху идет поиск работ для исполнителя
"""

'''
###########    снизу идет подборка предмета
'''
@dp.callback_query_handler(lambda c: c.data == 'customer_button_1')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали гуманитария: ')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳ : ',reply_markup=customer_keyboard2())
    global a
    a = 'Гуманитарий'

@dp.callback_query_handler(lambda c: c.data == 'customer_button_2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Программиста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',reply_markup=customer_keyboard2())
    global a
    a = 'Программист'

@dp.callback_query_handler(lambda c: c.data == 'customer_button_3')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Юриста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',reply_markup=customer_keyboard2())
    global a
    a = 'Юрист'

@dp.callback_query_handler(lambda c: c.data == 'customer_button_4')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Технаря :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',reply_markup=customer_keyboard2())
    global a
    a = 'Технарь'

@dp.callback_query_handler(lambda c: c.data == 'customer_button_5')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Естественника :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',reply_markup=customer_keyboard2())
    global a
    a = 'Естественник'

@dp.callback_query_handler(lambda c: c.data == 'customer_button_6')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали Экономиста :')
    await bot.send_message(callback_query.from_user.id, 'Ожидаемое время исполнения заказа ⏳: ',reply_markup=customer_keyboard2())
    global a
    a = 'Экономист'

@dp.callback_query_handler(lambda c: c.data == 'back2')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    #await bot.send_message(callback_query.from_user.id, 'Вы вернулись к выбору направления :')
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись к выбору направления, выберите направление :', reply_markup=customer_keyboard1())


'''
####       сверху идет подборка предмета
'''



"""
####      снизу идёт подборка даты      
"""

@dp.callback_query_handler(lambda c: c.data == 'customer_button_7')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант как можно скорее :')
    await bot.send_message(callback_query.from_user.id, 'Введите ожижаемую стоимость 💵: ', reply_markup=customer_keyboard3())
    global data
    data = 0
    data = datetime.datetime.now() + datetime.timedelta(days=0)

@dp.callback_query_handler(lambda c: c.data == 'customer_button_8')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант 1-2 дня :')
    await bot.send_message(callback_query.from_user.id, 'Введите ожижаемую стоимость 💵: ',
                           reply_markup=customer_keyboard3())
    global data
    data = datetime.datetime.now() + datetime.timedelta(days=2)

@dp.callback_query_handler(lambda c: c.data == 'customer_button_9')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант 2-4 дня :')
    await bot.send_message(callback_query.from_user.id, 'Введите ожижаемую стоимость 💵: ',
                           reply_markup=customer_keyboard3())
    global data
    data = datetime.datetime.now() + datetime.timedelta(days=4)

@dp.callback_query_handler(lambda c: c.data == 'customer_button_10')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали вариант в течение 7 дней :')
    await bot.send_message(callback_query.from_user.id, 'Введите ожижаемую стоимость 💵: ',
                           reply_markup=customer_keyboard3())
    global data
    data = datetime.datetime.now() + datetime.timedelta(days=7)


@dp.callback_query_handler(lambda c: c.data == 'customer_button_11')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите пероид исполнения заказа (в днях) ⏳')
    await Customer.question1.set()


@dp.callback_query_handler(lambda c: c.data == 'back3')
async def process_for_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы вернулись к выбору даты: ')
    await bot.send_message(callback_query.from_user.id, 'Выберите дату: ', reply_markup=customer_keyboard2())

"""
####     Сверху идёт подборка даты       
"""





"""
####    Снизу идет подборка цен
"""

@dp.callback_query_handler(lambda c: c.data == 'customer_button_12')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 100 рублей')
    global price
    price = 100
    sleep(0.5)
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_13')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 200 рублей')
    global price
    price = 200
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_14')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 300 рублей')
    global price
    price = 300
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_15')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 400 рублей')
    global price
    price = 400
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_16')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 500 рублей')
    global price
    price = 500
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_17')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 600 рублей')
    global price
    price = 600
    await bot.send_message(callback_query.from_user.id, 'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_18')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 700 рублей')
    global price
    price = 700
    await bot.send_message(callback_query.from_user.id,'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_19')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 800 рублей')
    global price
    price = 800
    await bot.send_message(callback_query.from_user.id, 'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_20')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 900 рублей')
    global price
    price = 900
    await bot.send_message(callback_query.from_user.id, 'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_21')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1000 рублей')
    global price
    price = 1000
    await bot.send_message(callback_query.from_user.id, 'Опишите задание: ')
    await Customer.question4.set()

@dp.callback_query_handler(lambda c: c.data == 'customer_button_22')
async def process_for_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите вашу цену (в рублях): ')
    global price
    await Customer.question2.set()


"""
####    Сверху идет подборка цен
"""
@dp.callback_query_handler(lambda c: c.data == 'button_3')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваши работы:', reply_markup=inlinekeyboard_3())

@dp.callback_query_handler(lambda c: c.data == 'button_4')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите профессиональное ориентирование или '
                                                        'выберите список работ которые можно '
                                                        'взять :', reply_markup=inlinekeyboard_4())
@dp.callback_query_handler(lambda c: c.data == 'button_5')
async def process_for_button_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Информация по Вашему профилю:')
    await bot.edit_message_reply_markup()



@dp.message_handler(commands=['start','начать'])
async def send_hello(message: types.message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!\n'
                         f'Задача этого сервиса -  помогать студентам и школьникам в учебе.\n'
                         f'Выполнение контрольных, задач, курсовых, рефератов и других заданий.\n'
                         f'Задания будут выполнять живые люди, а это значит, '
                         f'что преподаватель не сможет обвинить вас в списывании из интернета.\n'
                         f'Так же вы сможете самостоятельно выбирать себе помощника и договариваться с ним о стоимости работы.\n'
                         f'Или же стать помощником для кого-либо.\n'
                         f'Учитесь и зарабатывайте вместе с нами! '
                        ,reply_markup=implementer_inlinkeyboard())

@dp.message_handler(state=Customer.question1)  ### первое состяоние
async def send_text(message : types.message, state:FSMContext):
    answer = message.text
    global data
    if str(message.text).isdigit():
        data = datetime.datetime.now() + datetime.timedelta(days=int(answer))
    else:
        data = answer
    await state.update_data(answer1 = answer)
    sleep(1)
    await message.answer('Выберите желаемую стоимость: ', reply_markup=customer_keyboard3())
    global price
    price = answer
    await state.reset_state()


@dp.message_handler(state=Customer.question2) ## состояние второе (вводим приблизительну стоимость)
async def send_text(message : types.message, state:FSMContext):
    answer = message.text
    await state.update_data(answer2=answer)
    data1 = await state.get_data()
    answer1 = data1.get('answer1')
    answer2 = data1.get('answer2')

    global price
    price = answer2

    await message.answer('Опишите задание: ')
    await Customer.question4.set()


@dp.message_handler(state = Customer.question4)  #### состояние для введения текста
async def send_text(message: types.message, state:FSMContext):
    global order_text
    order_text = message.text
    await message.answer('Хотите прикрепить файл?', reply_markup=customer_keyboard_yes_no())
    await Customer.question3.set()

@dp.message_handler(state=Customer.question3)  ### третье состояние (для выбора да или нет)
async def send_text(message: types.document, state:FSMContext):
    answer = message
    if message.text == 'Да':
        await Customer.question5.set()
    else:
        await message.answer('Хорошо!\nВаш заказ принят!')
        add_to_database_customer(name = message.from_user.username, chat_id=message.from_user.id,
                                 subject=a, deadline=data, price=price, order_text=order_text,)
    await state.update_data(answer3 = answer)
    data1 = await state.get_data()

@dp.message_handler(content_types=['document'], state=Customer.question5) ### для отправки документа
async def get_file(message):
    await message.answer('Вы находитесь в состояннии 5, файл отправлен')
    text = ''
    file_info = await bot.get_file(message.document.file_id)
    await message.answer(message.document.file_name)
    ##  ↓↓↓↓↓↓↓ алгоритм для определения формата файла
    file_type = str(message.document.file_name).split('.')
    ##  ↑↑↑↑↑↑↑ алгоритм для определения формата файла
    downloaded_file = await bot.download_file(file_info.file_path)
    global file_content
    file_content = downloaded_file.read()
    print(len(file_content))
    add_to_database_customer(name=message.from_user.username, chat_id=message.from_user.id,
                             subject=a, deadline=data, price=price, order_text=order_text,file_path=file_content,
                             file_type = str(file_type[-1]))

    #await message.answer(text)


executor.start_polling(dp, on_startup=on_startup)