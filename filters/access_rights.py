from aiogram.types import Message
from aiogram.filters import BaseFilter
from database.admin import get_id_admins


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        probably_admin_id = message.chat.id
        return any(
            map(
                lambda admin_id: admin_id == probably_admin_id,
                get_id_admins()
            )
        )
        