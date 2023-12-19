from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from filters.access_rights import AdminFilter

router = Router()
router.message.filter(AdminFilter())

@router.message(Command("generate_key", 'gk'))
async def cmd_generate_key(message: Message):
    from auxiliary_functions.files_working import try_generate_key
    data_list = message.text.split()
    if len(data_list) != 2:
            await message.reply('Задан не верный формат ввода.')
            return 0
    value = data_list[1]
    if not value.isdigit():
            await message.reply('Второй аргумент должен быть числом.')
            return 0
    if not (bad_result:=try_generate_key(value)):
        await message.reply(f'Я успешно сгенерировала {value} ключей')
    else:
        await message.reply(bad_result)   