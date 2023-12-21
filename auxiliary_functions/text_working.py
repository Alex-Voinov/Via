def msg(word_comparison: str):
    from aiogram.types import Message
    def inner_msg(msg: Message):
        return word_comparison == msg.text.lower().strip()
    return inner_msg

def beautiful_text(text: str) -> str:
    SENTENCE_END_CHARS = (
        '.',
        '!',
        '?',
        '...'
    )
    '''Символы конца строки.'''
    PUNCTUATION_MARKS = {
        '-': '-',
        '–': ' – ',
        '—': ' — ',
        ',': ', ',
        ':': ': ' 
    }
    '''Знаки пунктуации и их правильное оформление.'''
    
    suggestions = ''
    for char in text.strip():
        if char.isdigit() or char.isalpha():
            suggestions += char 
            continue
        if char == ' ':
            if suggestions[-1] == ' ':
                continue
            else: 
                suggestions += ' '
                continue
        if char in PUNCTUATION_MARKS:
            ...
            continue
        if char 