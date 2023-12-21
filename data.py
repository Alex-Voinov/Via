from os.path import abspath, split, join

KEY_BASE_TITLE = 'keys.txt'
KEY_BASE_PATH: str =  join(split(abspath(__file__))[0], KEY_BASE_TITLE)
NOTIFICATION = False
LENG_KEY = 30

ADMINS_ID = [
    963467043,
    671674126
]