import re

def is_gibberish(text):
    text = re.sub(r'[^\w\s]', '', text)  # Убрать пунктуацию и пробелы
    text = re.sub(r'\s+', '', text)
    
    if not text.isalpha():     # Проверить то что там только буквы
        return False
    
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    if not any(char in vowels for char in text):     # Есть ли хотя бы одна гласная буква
        return False
    
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    if not any(char in consonants for char in text):     # Есть ли хотя бы одна не гласная буква
        return False
    
    return True

test_cases = [
    ('ыдвшоаыолвтас', False),
    ('ля ля ля ля ля', False),
    ('good', False),
    ('123', False),
    ('👍', False),
    ('Все ок', True),
    ('было челенджево, но суперски. респект', True),
    ('1. Интересно 2. Креативно 3. всё понятно.', True)
]

for text, expected_result in test_cases:
    result = is_gibberish(text)
    print(f'{text}: {result} (expected: {expected_result})')
