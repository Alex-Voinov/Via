from os.path import abspath, split, join

KEY_BASE_TITLE = 'keys.txt'
'''Название файла модержащего прайм-ключи.'''
KEY_BASE_PATH: str =  join(split(abspath(__file__))[0], KEY_BASE_TITLE)


NOTIFICATION = False
'''Отправка уведомлений в чат админам.'''
DEBAG = True
'''Отправка ошибок в чат админам.'''
LENG_KEY = 30
'''Длинна прайм-ключей.'''


ADMINS_ID = (
    963467043,
    671674126
)
'''Получают уведомления о работе бота и его ошибках.'''

SUPPORTS_ID = (
    963467043,
    671674126
)
'''Получают сообщения от людей, обращающихся в поддержку.'''