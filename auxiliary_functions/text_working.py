def msg(word_comparison: str):
    from aiogram.types import Message
    def inner_msg(msg: Message):
        return word_comparison == msg.text.lower().strip()
    return inner_msg