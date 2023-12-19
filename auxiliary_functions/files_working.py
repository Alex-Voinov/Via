def try_generate_key(amount_key: int) -> str:
    from data import KEY_BASE_PATH, LENG_KEY
    from random import choice
    from string import ascii_lowercase as letters

    try:
        secret_keys = []
        for _ in range(int(amount_key)):
            secret_keys.append(''.join(choice(letters) for _ in range(LENG_KEY)))
        with open(KEY_BASE_PATH, 'wt', encoding='utf-8') as key_file:
            print(*secret_keys, sep='\n', end='', file=key_file)

    except Exception as e:
        return str(e)
    return ''
