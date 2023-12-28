from aiogram.fsm.state import StatesGroup, State

class User_answer(StatesGroup):
    contacting_support = State()
    confirmation_support_message = State()
    write_name = State()
    write_email = State()
