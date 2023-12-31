DB_TITLE = 'mDataBase'
'''Название файла содержащего базу данных.'''


TOTAL_LEVELS_PRIVILEGES = 3
'''Колличество уровней привелегий.'''


NEW_KEY_DELEY_CHECK = 600
'''Частота проверки колличества свободных ключей.'''
NEW_KEY_GENERATION_THRESHOLD = 5
'''Минимальное колличество ключей, для генерации новых.'''
NEW_KEY_ONETIME_ISSUE = 100
'''Колличество ключей генерируемых за раз автоматически'''


ADMIN_GENERATE_NEW_KEY_MIN_AMOUNT = 1
'''Минимальное число ключей генерации за раз админом.'''
ADMIN_GENERATE_NEW_KEY_MAX_AMOUNT = 100
'''Максимальное число ключей генерации за раз админом.'''


NOTIFICATION = False
'''Отправка уведомлений в чат админам.'''
DEBAG = True
'''Отправка ошибок в чат админам.'''
LENG_KEY = 30
'''Длинна прайм-ключей.'''


MAX_LEN_ROW_MSG = 40
'''Максимальная длинна строки в сообщение.'''

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