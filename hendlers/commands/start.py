from aiogram import types

from app import dp


@dp.message_handler(commands=['start','начать'])
async def send_hello(message: types.message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!\n'
                         f'Задача этого сервиса -  помогать студентам и школьникам в учебе. '
                         f'Выполнение контрольных, задач, курсовых, рефератов и других заданий.'
                         f'Задания будут выполнять живые люди, а это значит, '
                         f'что преподаватель не сможет обвинить вас в списывании из интернета. '
                         f'Так же вы сможете самостоятельно выбирать себе помощника и договариваться с ним о стоимости работы. '
                         f'Или же стать помощником для кого-либо.'
                         f'Учитесь и зарабатывайте вместе с нами! \n'

                        )
    await message.answer(message.text, reply_markup=inlinkeyboard())