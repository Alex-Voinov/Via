async def send_ntf_admins(ntf: str):
    from data import NOTIFICATION, ADMINS_ID
    from main import bot
    if NOTIFICATION:
        for admin_id in ADMINS_ID:
            await bot.send_message(admin_id, ntf)