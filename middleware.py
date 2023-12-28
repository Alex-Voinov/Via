from typing import Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from database import create_new_msg
from aiogram.types import Message


class Add_msg_in_DB(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, any]], Awaitable[any]],
        event: TelegramObject,
        data: dict[str, any]
    ) -> any:
        if isinstance(event, Message):
            user_id =  event.from_user.id
            msg_id = event.message_id
            text = event.text
            username = event.from_user.full_name
            create_new_msg(user_id, msg_id, text, username)
        result = await handler(event, data)
        return result
