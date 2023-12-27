from aiogram import Router
from aiogram.types import Message
from auxiliary_functions.text_working import msg
from aiogram.fsm.context import FSMContext
from handlers.models import User_answer
from aiogram import types

router = Router()


@router.message(msg("что ты умеешь?"))
async def cmd_prime(message: Message):
    await message.reply('Всё что ты пожелаешь')


@router.message(msg("напиши в поддержку"))
async def cmd_connect_moderator(message: Message, state: FSMContext):
    await message.answer(
        'Какое сообщение передать модератору?)',
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(User_answer.contacting_support)


@router.message(User_answer.confirmation_support_message, msg('я хочу его отредактировать'))
async def edit_msg_for_moderator(message: Message, state: FSMContext):
    ...  # Случай если письмо хотят отредактировать

@router.message(User_answer.confirmation_support_message, msg('нет'))
async def close_msg_for_moderator(message: Message, state: FSMContext):
    ...  # Случай если хотят отменить отправку письма

@router.message(User_answer.confirmation_support_message, msg('да'))
async def fetch_msg_for_moderator(message: Message, state: FSMContext): 
    from data import SUPPORTS_ID
    from main import bot
    from random import choice
    from auxiliary_functions.text_working import beautiful_text
    just_a_little = choice(('немного','чуть-чуть', 'слегка'))
    edited_it = choice((
        'перефразировала',
        'подредактировала',
        'переформулировала',
        'изменила'
    ))
    disturb = choice((
        f'Извини, что {choice(("по",""))}тревожу',
        f'{choice(("Можно у","У"))}краду {choice(("у тебя ",""))}минутку?',
        f'Помоги {choice(("мне ",""))}пожалуйста'
    ))
    wrote_to_us = choice(('обратился в поддержку','написал нам', 'ждёт наш ответ'))
    data = await state.get_data()
    sent_message = data['support_request']
    await state.clear()
    sent_message_beautiful = beautiful_text(sent_message)
    start_message = f'''
{disturb}) 
Пользователь {message.from_user.full_name} {wrote_to_us} в {message.date.ctime()}.
'''
    if sent_message_beautiful[:-1] in sent_message[:-1]:
        end_message = f'Вот его сообщение:<i>\n«{sent_message_beautiful}»</i>.'
    else:
        end_message = f'''
Я {just_a_little} {edited_it} его сообщение: 
«<i>{sent_message_beautiful}</i>».
Вот исходный вариант: «<span class="tg-spoiler"><i>{sent_message}</i></span>».
'''
    try:
        for id in SUPPORTS_ID:
            await bot.send_message(id, start_message + end_message,
                parse_mode='html'
            )
    except:
        new_end = f'''Я {just_a_little} {edited_it} его сообщение: 
«{sent_message_beautiful}».
Вот исходный вариант:
 «{sent_message}».
    '''
        for id in SUPPORTS_ID:
            await bot.send_message(
                id, start_message.replace('<i>','').replace('</i>','') + new_end
            )
    finally:
        message_hb_sent = choice((
            'Я отправила сообщение, скоро тебе ответят)',
            "Уже отправила) Скоро нам ответят...",
            "Сообщение отправленно, можем развлекаться дальше)",
            'Готово, что прикажешь сделать теперь?)',
            'Готово, чем теперь займёмся?)',
        ))
        await message.answer(
            message_hb_sent,
            reply_markup=types.ReplyKeyboardRemove()
        )
        ... # Дописать взаимодействие с администратором

@router.message(User_answer.confirmation_support_message)
async def bad_answer_msg_for_moderator(message: Message, state: FSMContext):
    ... # Случай если некорректно ответили на вопрос об отправке письма


@router.message()
async def random_msg(message: Message):
    print('Случайное сообщение')

