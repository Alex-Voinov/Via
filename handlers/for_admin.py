from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from filters.access_rights import AdminFilter

router = Router()
router.message.filter(AdminFilter())

@router.message(Command("generate_key", 'gk'))
async def cmd_generate_key(message: Message):
    from database import generate_new_key
    from auxiliary_functions.msg_process import check_enter_command
    from data import ADMIN_GENERATE_NEW_KEY_MAX_AMOUNT, ADMIN_GENERATE_NEW_KEY_MIN_AMOUNT
    error, value = await check_enter_command(
        message,
        'число ключей',
        ADMIN_GENERATE_NEW_KEY_MIN_AMOUNT,
        ADMIN_GENERATE_NEW_KEY_MAX_AMOUNT,
        2
    )
    if not error:
        print(value)
        amount, lvl = value
        await generate_new_key(amount, message.from_user.id, lvl)
        await message.reply(f'Я успешно сгенерировала {amount} ключей')


@router.message(Command('issue_prime', 'ip'))
async def cmd_generate_key(message: Message):
        from auxiliary_functions.msg_process import check_enter_command
        from data import TOTAL_LEVELS_PRIVILEGES
        from database import issue_prime 
        error, value = await check_enter_command(
            message,
            'уровень доступа',
            1,
            TOTAL_LEVELS_PRIVILEGES
        )
        if not error:
            prime_kay = issue_prime(message.from_user.id, value)
            if not prime_kay:
                await message.reply('Что-то пошло не так...')
            else:
                await message.reply(f'''
Достала для тебя ключ активации прайм-аккаунта ^^
Ключ: {prime_kay}.
Уровень доступа: {value}.'''
                )