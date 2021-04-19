from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("items", "Вызов покупки..."),  # purchase
        types.BotCommand("menu", "Вызвать кнопки (Inline-кнопки)"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("privat", "Группа"),
        types.BotCommand("test", "Временное"),  # testing
        types.BotCommand("secret", "Команда для админов"), # admin
        types.BotCommand("get_cat","Получи котика ааааааа"),
        types.BotCommand("more_cats", "Получи больше котиков")

    ])