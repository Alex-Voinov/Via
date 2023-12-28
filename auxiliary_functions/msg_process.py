from aiogram.types import Message
from typing import Optional

async def check_enter_command(
        message: Message,
        text_ntf: str='число',
        min_number: Optional[int]=None,
        max_number: Optional[int]=None,
        amount_agrs: int=1
    ) -> tuple[bool, list[int] | int]:
    '''
Проверка ввода команды пользователем, формата /command number(s).

Объект message - првоеряемое сообщение пользователем.

*text_ntf - описание того, за что будет отвечать number.

*min_number и max_number - диапозон вводимого числа, если он нужен.

*amount_agrs - Общее число аргументов после команды, если их больше одного

Возвращает кортеж из True/False (статус ошибки) и integer(ведённого числа).
    '''
    
    def check(value: str, number: Optional[int]=None) -> str:
        '''
        Внутренняя функция для проверки диапазона 
        и типа одного введеного параметра.
        '''
        potentional_number = "" if not number else f"№{number} "
        if not (value.isdigit() or (value[0]=='-' and value[1:].isdigit())):
            return f'Аргумент {potentional_number}должен быть числом.' 
        value = int(value)
        if (type(max_number) is int and value > max_number ):
            return f'Параметр {potentional_number}должен быть меньше {max_number}'
        if (type(min_number) is int and value < min_number):
            return f'Параметр {potentional_number}должен быть больше {min_number}'
        return ''
    
    data_list = message.text.split()
    entered_args = len(data_list) - 1
    if entered_args != amount_agrs or not entered_args:
        notification = (
            f"Пожалуйста, укажи {(f'только {text_ntf}' if amount_agrs == 1 else f'{amount_agrs} аргументов')}"
            f" после команды {data_list[0]}"
        )
        await message.reply(notification)
        return True, 0
    if amount_agrs == 1:
        potentional_value = data_list[1]
        check_error = check(potentional_value)
        if check_error:
            await message.reply(check_error)
            return True, 0
        return False, int(potentional_value)
    values: list[int] = []
    erorrs: list[str] = []
    for number, value in enumerate(data_list[1:]):
        check_error = check(value, number + 1)
        if check_error:
            erorrs.append(check_error)
        elif not check_error:
            values.append(int(value))
    if not erorrs:
        return False, values
    if len(erorrs) == 1:
        notification = f'Упс, ошибочка! Подправь пожалуйста:\n{erorrs[0]}'
    else:
        errors = '\n'.join(map(lambda e, n: f'\t{n+1}) {e}' , erorrs, range(len(erorrs))))
        notification = f"Надо кое-что подправить:\n{errors}"
        await message.reply(notification)
    return True, 0
    

    
    
      