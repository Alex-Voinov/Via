def msg(word_comparison: str):
    from aiogram.types import Message
    def inner_msg(msg: Message):
        return word_comparison == msg.text.lower().strip()
    return inner_msg


def is_bad_word(probably_bad_word: str) -> bool:
    SIMILAR_CHARACTERS = {
        '4': 'ч',
        '6': 'б',
        'k': 'к',
        'a': 'а',
        'b' : 'б',
        's': 'с',
        'x': 'х',
        'y': 'у',
        'u': 'у',
        'e': 'е',
        'w': 'ш',
        'ё': 'е',
        'r': 'р',
        'p': 'р',
        'h': 'н',
        'l': 'л',
        'd': 'д',
        'j': 'ж',
        'й': 'и',
        '7': 'г',
        'j': 'ж',
        'o': 'о',
        'g': 'г',
        'i': 'и'
    }
    BAD_WORDS = (
        'сук',
        'уеб',
        'пизд',
        'пидор',
        'пидр',
        'пидар',
        'жоп',
        'хуе',
        'хуи',
        'говн',
        'дерь',
        'ебат',
        'ебан',
        'ебал',
        'сучк',
        'долба',
    )
    for charter, simalr_charter in SIMILAR_CHARACTERS.items():
        probably_bad_word = probably_bad_word.replace(charter, simalr_charter)
    probably_bad_word = ''.join(tuple(filter(str.isalpha, probably_bad_word)))
    for bad_word in BAD_WORDS:
        if bad_word in probably_bad_word.lower():
            return True
    return False


def is_bad_word(probably_bad_word: str) -> bool:
    SIMILAR_CHARACTERS = {
        '4': 'ч',
        '6': 'б',
        'k': 'к',
        'a': 'а',
        'b' : 'б',
        's': 'с',
        'x': 'х',
        'y': 'у',
        'u': 'у',
        'e': 'е',
        'w': 'ш',
        'ё': 'е',
        'r': 'р',
        'p': 'р',
        'h': 'н',
        'l': 'л',
        'd': 'д',
        'j': 'ж',
        'й': 'и',
        '7': 'г',
        'j': 'ж',
        'o': 'о',
        'g': 'г',
        'i': 'и'
    }
    BAD_WORDS = (
        'сук',
        'уеб',
        'пизд',
        'пидор',
        'pи',
        'pi',
        'пидр',
        'пидар',
        'жоп',
        'хуе',
        'хуи',
        'говн',
        'дерь',
        'ебат',
        'ебан',
        'ебал',
        'сучк',
        'долба',
        'отсос'
    )
    for charter, simalr_charter in SIMILAR_CHARACTERS.items():
        probably_bad_word = probably_bad_word.replace(charter, simalr_charter)
    probably_bad_word = ''.join(tuple(filter(str.isalpha, probably_bad_word)))
    for bad_word in BAD_WORDS:
        if bad_word in probably_bad_word.lower():
            return True
    return False


def is_bad_word(probably_bad_word: str) -> bool:
    SIMILAR_CHARACTERS = {
        '4': 'ч',
        '6': 'б',
        'k': 'к',
        'a': 'а',
        'b' : 'б',
        's': 'с',
        'x': 'х',
        'y': 'у',
        'u': 'у',
        'e': 'е',
        'w': 'ш',
        'ё': 'е',
        'r': 'р',
        'p': 'р',
        'h': 'н',
        'l': 'л',
        'd': 'д',
        'j': 'ж',
        'й': 'и',
        '7': 'г',
        'j': 'ж',
        'o': 'о',
        'g': 'г',
        'i': 'и'
    }
    BAD_WORDS = (
        'сук',
        'уеб',
        'пизд',
        'пидор',
        'пидр',
        'пидар',
        'жоп',
        'хуе',
        'хуи',
        'говн',
        'дерь',
        'ебат',
        'ебан',
        'ебал',
        'сучк',
        'долба',
        'отсоси',
    )
    for charter, simalr_charter in SIMILAR_CHARACTERS.items():
        probably_bad_word = probably_bad_word.replace(charter, simalr_charter)
    probably_bad_word = ''.join(tuple(filter(str.isalpha, probably_bad_word)))
    for bad_word in BAD_WORDS:
        if bad_word in probably_bad_word.lower():
            return True
    return False


def beautiful_text(text: str) -> str:
   SENTENCE_END_CHARS = (
   '.',
   '!',
   '?',
   )
   PUNCTUATION_MARKS_WITHOUT_SPACE = (
   '-',
   '/',
   '№',
   '@',
   '*',
   )
   PUNCTUATION_MARKS_SPACE_BEFORE = (
   '#',
   )
   PUNCTUATION_MARKS_SPACE_AFTER = (
   ',',
   ':',
   ';',
   )
   PUNCTUATION_MARKS_SPACE_BEFORE_AFTER = (
   '–',
   '—',
   '=',
   '>',
   '<',
   )
   PUNCTUATION_MARKS = (
      *PUNCTUATION_MARKS_WITHOUT_SPACE, 
      *PUNCTUATION_MARKS_SPACE_BEFORE,
      *PUNCTUATION_MARKS_SPACE_AFTER,
      *PUNCTUATION_MARKS_SPACE_BEFORE_AFTER
   )
   '''Символы конца строки.'''
   suggestions = ''
   word = ''
   total_msg =''
   completed_text = text.strip()
   if completed_text[-1] not in SENTENCE_END_CHARS: 
      completed_text += '.'
   for char in completed_text:
      if char.isdigit() or char.isalpha():
         bad_result = False
         if word:
            amount_repeat = 0
            for char_from_end in reversed(word):
               if char_from_end == char:
                  amount_repeat += 1
                  if amount_repeat > 2:
                     bad_result = True
                     break
         if not bad_result:      
            word += char
      elif char == ' ' and not (suggestions and suggestions[-1] == ' '):
         if is_bad_word(word): word = '***'
         suggestions += (" " if suggestions and word else '') + word
         word = ''
      elif char in PUNCTUATION_MARKS_WITHOUT_SPACE or char in PUNCTUATION_MARKS_SPACE_AFTER:
         if word == '' and not suggestions[-1] in PUNCTUATION_MARKS:
            suggestions += char
         else:
            if is_bad_word(word): word = '***'
            suggestions += (" " if suggestions and word else '') + word + char
            word = ''
      elif char in PUNCTUATION_MARKS_SPACE_BEFORE:
         if word == '' and not suggestions[-1] in PUNCTUATION_MARKS:
            suggestions += ' ' + char
         else:
            if is_bad_word(word): word = '***'
            suggestions += word + ' ' + char
            word = ''
      elif char in PUNCTUATION_MARKS_SPACE_BEFORE_AFTER:
         if suggestions:
            if char == '<':
               if suggestions[-1] == '<': suggestions = suggestions[:-1] + '«' 
            if char == '>':
               if suggestions[-1] == '>': suggestions = suggestions[:-1] + '»'
            if word == '' and not suggestions[-1] in PUNCTUATION_MARKS:
               suggestions += ' ' + char
         else:
            if is_bad_word(word): word = '***'
            suggestions += word + ' ' + char
            word = ''
      elif char in SENTENCE_END_CHARS and (suggestions or word): #добавил or word. Проверь, ничего ли не ломается!
         if is_bad_word(word): word = '***'
         total_msg += (" " if total_msg else '') + (
            suggestions + (" " if suggestions and word else '') + word
            ).capitalize() + char
         word = ''
         suggestions = ''
   while '<' in total_msg and '>' in total_msg:
      total_msg = total_msg[:total_msg.index('<')] + total_msg[total_msg.index('>') + 1:]
   print(total_msg)
   return total_msg