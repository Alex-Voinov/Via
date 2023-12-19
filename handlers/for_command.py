from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()

@router.message(Command("info"))
async def cmd_start(message: Message):
    info_msg: str = f'''
Ваш id: {message.from_user.id}
Полноем имя вашего профиля: {message.from_user.full_name}
Ваш язык: {message.from_user.language_code}
'''
    await message.answer(info_msg)


@router.message(Command("prime"))
async def cmd_prime(message: Message):
    from main import KEY_BASE_TITLE
    #######
    SECRET_KEYS = (key.strip() for key in open(KEY_BASE_TITLE, 'rt', encoding='utf-8'))
    await message.reply(" ".join(SECRET_KEYS))


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    from main import START_TIME
    from data import KEY_BASE_PATH
    from datetime import datetime as D
    amount_key = len(open(KEY_BASE_PATH, 'rt', encoding='utf-8').readlines())
    await message.reply(f'''
Общая статистика сессии Via:
    Время запуска: {START_TIME.strftime("%Y-%m-%d %H:%M")}
    Время работы: {str(D.now() - START_TIME).split('.')[0]}
    Колличество свободных prime-ключей: {amount_key}
''')

@router.message(Command('clear', 'cls'))
async def cmd_clear(message: Message):
    from asyncio import sleep
    from main import bot
    await message.answer('Дай мне секундочку...')
    await sleep(2)
    print('Start clearing messages!!!')
    for i in range(message.message_id, 0, -1):
        try:  
            await bot.delete_message(message.from_user.id, i)
            print(i)
        except: i = 1
    print(message.message_id + 1)
    await bot.delete_message(message.from_user.id, message.message_id + 1)


