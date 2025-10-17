


tokonize_test_case = [
  "привет мир",        # ["привет", "мир"
  "hello,world!!!",    # ["hello", "world"]
  "по-настоящему круто", # ["по-настоящему", "круто"]
  "2025 год",          # ["2025", "год"]
  "emoji 😀 не слово"   # ["emoji", "не", "слово"]
]



def tokenize(text: str) -> list[str]:
    import re
    
    p = r'\w+(?:-\w+)*'
    tokens = re.findall(p, text) # проверяем совпадения в нашей строке и возвращаем их список
    return tokens

for i in tokonize_test_case:
    print(tokenize(i))
    