async def send_ntf_admins(ntf: str):
    from data import NOTIFICATION
    from database.admin import get_id_admins
    from main import bot
    if NOTIFICATION:
        for admin_id in get_id_admins:
            await bot.send_message(admin_id, ntf)

async def send_error_admins(error: str):
    from data import DEBAG
    from main import bot
    from database.admin import get_id_admins
    if DEBAG:
        for admin_id in get_id_admins():
            await bot.send_message(admin_id, error)