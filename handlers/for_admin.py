from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from filters.access_rights import AdminFilter
from database import add_admin_this_request
from aiogram.fsm.context import FSMContext
from handlers.models import User_answer
from main import bot

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

@router.message(Command("make_admin", "ma"))
async def cmd_make_admin(message: Message, state: FSMContext):
        info = message.text.split()
        bot.send_message(info[1], 'Доброго времени суток. Вас хотят сделать амнимистратором. Введите допольнительную информацию о себе. Как вас зовут (Имя Фамилия)?')
        await state.set_state(User_answer.write_name)
        data = await state.get_data()
        user_name = data['write_name']
        user_email = data['write_email']
        await state.clear()
        add_admin_this_request(info[1], user_name, message.from_user.id, user_email)