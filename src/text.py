def count_freg(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество вхождений каждого слова в списке токенов.

    Args:
        tokens (list[str]): Список токенов (слов), полученных из текста.

    Returns:
        dict[str, int]: Словарь, где ключ — слово, а значение — количество его вхождений.
    """
    from collections import Counter
    return dict(Counter(tokens))  # считаем частоты элементов 


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: убирает управляющие символы, заменяет 'ё' на 'е', приводит к нижнему регистру.

    Args:
        text (str): Исходный текст.
        casefold (bool, optional): Приводить ли текст к нижнему регистру (по умолчанию True).
        yo2e (bool, optional): Заменять ли 'ё' на 'е' (по умолчанию True).

    Returns:
        str: Нормализованный текст.
    """
    control_character = ['\n', '\t', '\r']
    for char in control_character:
        text = text.replace(char, ' ')
    words = text.split()
    text = ' '.join(words)

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    if casefold:
        text = text.casefold()
    
    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на токены (слова), поддерживая дефисные слова.

    Примеры токенов: "мама", "папа", "поезда-характеристики"

    Args:
        text (str): Входной текст.

    Returns:
        list[str]: Список токенов (слов), извлечённых из текста.
    """
    import re
    p = r'\w+(?:-\w+)*'
    tokens = re.findall(p, text)  # проверяем совпадения в нашей строке и возвращаем их список
    return tokens


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N слов по убыванию частоты, при равенстве — по алфавиту.

    Args:
        freq (dict[str, int]): Словарь частот слов.
        n (int, optional): Количество наиболее частых слов для возврата (по умолчанию 5).

    Returns:
        list[tuple[str, int]]: Список кортежей (слово, частота), отсортированных по частоте и алфавиту.
    """
    my_list = list(freq.items())

    def sort_po_alfavity(key_v):
        return key_v[0]
    my_list.sort(key=sort_po_alfavity)

    def sort_po_num(key_v):
        return key_v[1]
    my_list.sort(key=sort_po_num, reverse=True)

    return my_list[:n]
