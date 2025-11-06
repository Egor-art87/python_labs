import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from src.text import tokenize, count_freg, top_n


table = True

def print_table(top: list[tuple]):
    """
    Выводит топ слов с их частотами в табличном формате.

    Форматирует таблицу с двумя столбцами: слово и частота.
    Ширина столбца "слово" подстраивается под максимальную длину слова из списка.

    Args:
        top (list[tuple[str, int]]): список кортежей (слово, частота)
    """
    max_len = max(len(word) for word, _ in top)
    col_word = 'слово'
    col_freq = 'частота'

    width_word = max(max_len, len(col_word))
    width_freq = len(col_freq)
    print(f"{col_word:<{width_word}} | {col_freq}")
    print("-" * width_word + "-+-" + "-" * width_freq)

    for word, count in top:
        print(f"{word:<{width_word}} | {count}")


def main():
    """
    Основная функция программы.

    Считывает текст из стандартного ввода, нормализует и токенизирует его,
    подсчитывает частоты слов и выводит общую статистику,
    а также топ-5 самых частотных слов в табличном или обычном формате
    в зависимости от флага 'table'.
    """
    
    print('Введите текс(для окончания ввода нажмите Ctrl+D (Linux/Mac) или Ctrl+Z Enter (Windows)):')
    text = sys.stdin.read()

    tokens = (tokenize(text))
    freq = (count_freg(tokens))

    print()
    print(f'Всего слов: {len(tokens)}')
    print(f'Кол-во уникальных слов {len(freq)}')

    top_5 = top_n(freq, 5)

    if table:
            print_table(top_5)
    else:
        print('Топ-5:', ' '.join(f"{word}:{count}" for word, count in top_5))

if __name__ == "__main__":
    main()
