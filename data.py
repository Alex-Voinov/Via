from os.path import abspath, split, join
KEY_BASE_TITLE = 'keys.txt'
KEY_BASE_PATH: str =  join(split(abspath(__file__))[0], KEY_BASE_TITLE)
print(KEY_BASE_PATH)
LENG_KEY = 30