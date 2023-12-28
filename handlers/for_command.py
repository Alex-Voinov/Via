from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()

@router.message(Command("info"))
async def cmd_start(message: Message):
    from database import get_user_info
    from data import MAX_LEN_ROW_MSG
    id_user = message.from_user.id
    user_info = get_user_info(id_user)
    prime_status = user_info.prime_status
    info_msg: str = f'''
Рассказать, что я о тебе знаю?)
\tИмя: {message.from_user.full_name:>{MAX_LEN_ROW_MSG - len('Имя: ')}}
\tУровень привелегий: {'отсутсвует' if not prime_status else prime_status:>{MAX_LEN_ROW_MSG - len('Уровень привелегий: ')}}
\tTellegram-id: {id_user:>{MAX_LEN_ROW_MSG - len('Tellegram-id: ')}}
\tЯзык: {message.from_user.language_code:>{MAX_LEN_ROW_MSG - len('Язык: ')}}
'''
    await message.answer(info_msg)


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    from main import START_TIME
    from datetime import datetime as D
    from database import get_amount_free_key
    print(123)
    await message.reply(f'''
Общая статистика сессии Via:
    Время запуска: {START_TIME.strftime("%Y-%m-%d %H:%M")}
    Время работы: {str(D.now() - START_TIME).split('.')[0]}
    Колличество свободных prime-ключей: {get_amount_free_key()}
''')


@router.message(Command('clear', 'cls'))
async def cmd_clear(message: Message):
    from main import bot
    from asyncio import sleep
    from database import messages_to_update
    msg_id = message.message_id
    user_id = message.from_user.id
    await message.answer('Дай мне секундочку...')
    await sleep(2)
    await messages_to_update(user_id)
    await bot.delete_message(user_id, msg_id + 1)


@router.message(Command('prime', 'activate'))
async def cmd_prime(message: Message):
    ...
