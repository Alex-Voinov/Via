from asyncio import run
from dotenv import dotenv_values
from logging import basicConfig, DEBUG
from aiogram import Bot, Dispatcher 
from datetime import datetime as D
from handlers import (
    for_command,
    for_keybords,
    for_admin,
    for_text
)


START_TIME = D.now()
ENV = dotenv_values('.env')
ADMIN_ID = ENV['admin_id']
TOKEN = ENV['token']
bot = Bot(TOKEN)
dp = Dispatcher()
basicConfig(level=DEBUG)


async def main():  

    try:
        dp.include_routers(
            for_keybords.router,
            for_command.router,
            for_text.router,
            for_admin.router,
        )

        await bot.delete_webhook(drop_pending_updates=True)
        await bot.send_message(ADMIN_ID, 'Via была запущена')
        await dp.start_polling(bot)

    except Exception as error:
        print(error)

    finally:
        await bot.send_message(ADMIN_ID, 'Via была отключена')
        await bot.session.close()



if __name__ == "__main__":
    run(main())