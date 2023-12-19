from aiogram.types import Message
from main import ADMIN_ID
from aiogram.filters import BaseFilter


class AdminFilter(BaseFilter):
    __ADMIN_ID: int 
    def __init__(self):
        self.__ADMIN_ID = int(ADMIN_ID)
    async def __call__(self, message: Message) -> bool:
        if not (reslult := message.from_user.id == self.__ADMIN_ID):
            await message.reply ('У вас недостаточно прав доступа для этой команды')
        return reslult