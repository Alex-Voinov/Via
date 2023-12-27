from aiogram.types import Message


async def check_enter_command(message: Message, text_ntf: str):
   data_list = message.text.split()
   if len(data_list) != 2:
         await message.reply(f'''
Пожалуйста, укажи {text_ntf} через пробел)
''')
         return True, 0
   value = data_list[1]
   if not value.isdigit():
         await message.reply('Второй аргумент должен быть числом.')
         return True, 0
   return False, value