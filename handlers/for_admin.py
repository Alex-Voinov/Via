from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from filters.access_rights import AdminFilter

router = Router()
router.message.filter(AdminFilter())

@router.message(Command("generate_key", 'gk'))
async def cmd_generate_key(message: Message):
    from database import generate_new_key
    data_list = message.text.split()
    if len(data_list) != 2:
            await message.reply('Задан не верный формат ввода.')
            return 0
    value = data_list[1]
    if not value.isdigit():
            await message.reply('Второй аргумент должен быть числом.')
            return 0
    await generate_new_key(int(value), message.from_user.id, 1)
    await message.reply(f'Я успешно сгенерировала {value} ключей')
    