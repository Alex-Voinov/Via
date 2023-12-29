async def check_exist_free_key():
    from database.secret_key import generate_new_key, get_amount_free_key
    from asyncio import sleep
    from data import (
        NEW_KEY_DELEY_CHECK,
        NEW_KEY_GENERATION_THRESHOLD,
        NEW_KEY_ONETIME_ISSUE,
        TOTAL_LEVELS_PRIVILEGES
    )
    while True:
        for privilegies_lvl in range(1, TOTAL_LEVELS_PRIVILEGES + 1):
            print(privilegies_lvl)
            print(get_amount_free_key(privilegies_lvl))
            print(get_amount_free_key(privilegies_lvl) <= NEW_KEY_GENERATION_THRESHOLD)
            if get_amount_free_key(privilegies_lvl) <= NEW_KEY_GENERATION_THRESHOLD:
                generate_new_key(NEW_KEY_ONETIME_ISSUE, 0, privilegies_lvl) 
        await sleep(NEW_KEY_DELEY_CHECK)

TASKS = (
    check_exist_free_key(),
)