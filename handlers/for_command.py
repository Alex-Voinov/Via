from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from handlers.models import User_answer


router = Router()

@router.message(Command("info"))
async def cmd_start(message: Message):
    from database.user import get_user_info
    id_user = message.from_user.id
    user_info = get_user_info(id_user)
    prime_status = user_info.prime_status
    info_msg: str = f'''
Рассказать, что я о тебе знаю?)
\tИмя: {message.from_user.full_name}
\tУровень привелегий: {'отсутствует' if not prime_status else prime_status}
\tTellegram-id: {id_user}
\tЯзык: {message.from_user.language_code}
'''
    await message.answer(info_msg)


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    from main import START_TIME
    from datetime import datetime as D
    from database.secret_key import get_amount_free_key
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
    from database.message import messages_to_update
    msg_id = message.message_id
    user_id = message.from_user.id
    await message.answer('Дай мне секундочку...')
    await sleep(2)
    await messages_to_update(user_id)
    await bot.delete_message(user_id, msg_id + 1)


@router.message(Command('prime', 'activate'))
async def cmd_prime(message: Message, state: FSMContext):
    await message.answer(
        'Напиши мне свой ключ активации',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(User_answer.secret_key)

@router.message(User_answer.secret_key)
async def check_secret_key(message: Message, state: FSMContext):
    from database.secret_key import try_activate_prime
    success, status_code = try_activate_prime(message.text, message.from_user.id)
    if not success:
        if status_code == 0:
            await message.reply('Такого ключа не существует')
        elif status_code == 1:
            ...# написать модераторам/админу уведомление
        elif status_code == 2:
            await message.reply('Данный ключ уже был использован.')
            ...
    else:
        await message.reply(
            'Поздравляю! Ты успешно активировал prime-status!\n'
            f'Твой уровень привелегий: {status_code}'
        )
    await state.clear()
