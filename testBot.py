from aiogram import Bot, Dispatcher, types, executor

def main(first_id, second_id):
    my_token = '1624963008:AAExGpcC5y1W0Ea22DUhN0xhv3mq8P4BGrI'
    bot = Bot(token=my_token)
    dp = Dispatcher(bot)
    @dp.message_handler(content_types=['text'])
    async def send_text(message):
        answer = message.text
        if int(message.from_user.id) == int(first_id):
            await bot.send_message(second_id, answer)
        elif int(message.from_user.id) == int(second_id):
            await bot.send_message(first_id, answer)
    executor.start_polling(dp)
