from aiogram import Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [KeyboardButton(text="Что ты умеешь?")],
        [KeyboardButton(text="Свяжи с модераторами")],
        [KeyboardButton(text="Активируй prime-status")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer('Поиграешь со мной?', reply_markup=keyboard)