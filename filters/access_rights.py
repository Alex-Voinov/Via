from aiogram.types import Message
from data import ADMINS_ID
from aiogram.filters import BaseFilter


class AdminFilter(BaseFilter):
    __ADMINS_ID: list[int] 
    def __init__(self):
        self.__ADMINS_ID = ADMINS_ID
    async def __call__(self, message: Message) -> bool:
        probably_admin_id = message.chat.id
        return any(
            map(
                lambda admin_id: admin_id == probably_admin_id,
                self.__ADMINS_ID
            )
        )
        