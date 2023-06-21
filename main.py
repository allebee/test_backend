import re
import emoji

def is_gibberish(text):
    # Удалить пунктуацию и пробелы
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', '', text)
    
    # Проверить, содержит ли текст только эмодзи
    if all(char in emoji.UNICODE_EMOJI for char in text):
        return True
    
    # Проверить, содержит ли текст только буквы
    if not text.isalpha():
        return False
    
    # Проверить, содержит ли текст хотя бы одну гласную букву
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    if not any(char in vowels for char in text):
        return False
    
    # Проверить, содержит ли текст хотя бы один согласный звук
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    if not any(char in consonants for char in text):
        return False
    
    return True

test_cases = [
    ('ыдвшоаыолвтас', False),
    ('ля ля ля ля ля', False),
    ('good', False),
    ('123', False),
    ('👍', True),
    ('Все ок', True),
    ('было челенджево, но суперски. респект', True),
    ('1. Интересно 2. Креативно 3. всё понятно.', True)
]

for text, expected_result in test_cases:
    result = is_gibberish(text)
    print(f'{text}: {result} (expected: {expected_result})')
