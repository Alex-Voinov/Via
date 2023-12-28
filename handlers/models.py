from aiogram.fsm.state import StatesGroup, State

class User_answer(StatesGroup):
    contacting_support = State()
    confirmation_support_message = State()
    secret_key = State()
