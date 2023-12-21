from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from handlers.models import User_answer

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    BUTTONS_TEXT = (
        'Что ты умеешь?',
        'Свяжи с модераторами',
        'Активируй prime-status',
    )
    kb = [[KeyboardButton(text=button_text)] for button_text in BUTTONS_TEXT]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer('Поиграешь со мной?', reply_markup=keyboard)


@router.message(User_answer.contacting_support)
async def fetch_msg_for_moderator(message: Message, state: FSMContext): 
    BUTTONS_TEXT = (
        'Да',
        'Я хочу его отредактировать',
        'Отмена',
    )
    kb = [ [KeyboardButton(text=button_text)] for button_text in BUTTONS_TEXT ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(f'''
Ты хочешь, чтобы я передала модератору сообщение:
"{message.text}"?
''',
    reply_markup=keyboard
    )
    await state.update_data(support_request=message.text)
    await state.set_state(User_answer.confirmation_support_message)
    
