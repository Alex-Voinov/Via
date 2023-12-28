from aiogram.types import Message
from typing import Optional

async def check_enter_command(
          message: Message,
          text_ntf: str='число',
          min_number: Optional[int]=None,
          max_number: Optional[int]=None,
      ):
      '''
Проверка ввода команды пользователем, формата /command number.

Объект message - првоеряемое сообщение пользователем.

*text_ntf - описание того, за что будет отвечать number.

*min_number и max_number - диапозон вводимого числа, если он нужен.

Возвращает кортеж из True/False (статус ошибки) и integer(ведённого числа).
      '''
      data_list = message.text.split()
      if len(data_list) != 2:
          await message.reply(f'''
Пожалуйста, укажи {text_ntf} через пробел)
''')
          return True, 0
      value = data_list[1]
      if not (value.isdigit() or (value[0]=='-' and value[1:].isdigit())):
          await message.reply('Второй аргумент должен быть числом.')
          return True, 0
      value = int(value)
      notification = ''
      if (type(max_number) is int and value > max_number ):
          notification = f'Параметр должен быть меньше {max_number}'
      if (type(min_number) is int and value < min_number):
          notification = f'Параметр должен быть больше {min_number}'
      if notification:
            await message.reply(notification)
            return True, 0
      return False, value
      