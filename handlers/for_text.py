from aiogram import Router
from aiogram.types import Message
from auxiliary_functions.text_working import msg
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()

class User_answer(StatesGroup):
    answer = State()


@router.message(msg("что ты умеешь?"))
async def cmd_prime(message: Message):
    await message.reply('Всё что ты пожелаешь')


@router.message(msg("свяжи с модераторами"))
async def cmd_connect_moderator(message: Message, state: FSMContext):
    await message.answer('''
Какое сообщение передать модератору?
Напишите его в  следующем сообщении.
''')
    await state.set_state(User_answer.answer)


@router.message(User_answer.answer)
async def fetch_msg_for_moderator(message: Message, state: FSMContext): 
    await message.reply(f'''
Ты хочешь, чтобы я передала модератору сообщение:
"{message.text}"?
'''
    )
    await state.clear()

