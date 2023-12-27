from asyncio import run, gather
from dotenv import dotenv_values
from logging import basicConfig, DEBUG
from aiogram import Bot, Dispatcher 
from datetime import datetime as D
from sending_messages.admin_msg import send_ntf_admins, send_error_admins
from database import initialize_db, db_close
from middleware import Add_msg_in_DB
from ongoing_processes import TASKS


from handlers import (
    for_command,
    for_keybords,
    for_admin,
    for_text
)


START_TIME = D.now()
ENV = dotenv_values('.env')
TOKEN = ENV['token']
bot = Bot(TOKEN)
dp = Dispatcher()
basicConfig(level=DEBUG)


async def main():  

    try:
        await initialize_db()
        dp.message.middleware(Add_msg_in_DB())
        await gather(*TASKS)
        dp.callback_query.middleware(Add_msg_in_DB())
        dp.include_routers(
            for_keybords.router,
            for_command.router,
            for_admin.router,
            for_text.router,
        )  
        await bot.delete_webhook(drop_pending_updates=True)
        await send_ntf_admins('Via была запущена')
        await dp.start_polling(bot)

    except Exception as error:
        print(error)
        #await send_error_admins(error)

    finally:
        await send_ntf_admins('Via была отключена')
        await bot.session.close()
        db_close()


if __name__ == "__main__":
    run(main())