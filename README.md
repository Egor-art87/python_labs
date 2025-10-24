# lab01

## Задача 1

Программа запрашивает имя и возрост, а затем вывод имя и возраст через год.  

![вывод_задача1](/images/lab01/01.png)

## Задача 2

Программа ищет сумму и среднее значение 

![Вывод_задача2](/images/lab01/02.png)

## Задача 3

Программа ищет базу полсе скидки, НДС и считает итоговую стоимомть 

![Вывод_задача3](/images/lab01/03.png)

## Задача 4

Программа переаодит минуты в Часы:Минуты

![Вывод_задача4](/images/lab01/04.png)

## Задача 5

Программа запрашивает ФИО, инициалы, убирает лишние пробелы, ФИО всегда выводит в верхнем регистре

![Вывод_задача5](/images/lab01/05.png)

## Задача 6

Программа считает учеников на очной и заочной форме образования

![Вывод_задача6](/images/lab01/06.png)

## Задача 7

Программа расшифровывает шифр

![Вывод_задача5](/images/lab01/07.png)


# lab02

## Задача A

### 1 пункт

Проверяю, что списко больше 0, если он больше нуля программа возвращает кортеж с мин и макс. Иначе выдаст ошибку. 


```python
def min_max_iz_spiska(my_list): 
    if len(my_list) > 0:          
        my_list = sorted(my_list)
        minn = my_list[-1]
        maxx = my_list[0]
        min_max= []
        min_max.append(maxx)
        min_max.append(minn)
        return tuple(min_max)
    else:
        return ValueError
```

### 2 пункт

Использую встроенные функции и методы


```python
print('unique_sorted')

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    print(list(sorted(dict.fromkeys(nums))))
    
unique_sorted(list6)
unique_sorted(list7)
unique_sorted(list8)
unique_sorted(list9)
```

### 3 пункт 

Создаю пустой список, прохожусь по элементом первоначального списка, если i является списком или кортежем, добавляю её в пустой список. Иначе - ошибка  


```python
def raspl_row_major(elementary_list):
    result = []
    for i in elementary_list:
        if isinstance(i, (list, tuple)):
            result.extend(i)
        else:
            return TypeError(f'Элемент {i} не является списком или кортежем')
    return result
```

![Вывод_задача_A](/images/lab02/01.png)

## Задача B

### 1 пункт


```python
def transpose_compact(mat):
    if not mat:
        return []  # возращаю пустой список, если матрица пустая
    # проверяю, что матрица не рванная
    first_row = len(mat[0]) # беру эталонное значение 
    for row in mat: 
        if len(row) != first_row: # если длина row != этлону - ошибка 
            return ValueError('рванная')
        # формирую новую матрицу 
    res = []               # создаю пустой список 
    # определяю размеры исходной матрицы 
    num_cols = len(mat[0])  # кол-во столбцов 
    num_rows = len(mat)     # кол-во строк

    for col in range(num_cols): # прохожусь по всем стодбцам 
        new_row = []  # промежуточный список 
        for row in range(num_rows):  # прохожусь по всем строкам 
            new_row.append(mat[row][col])  # добавляю в новый список строки и стобцы 
        res.append(new_row) # добавляю промежуточный списко в конечный 
    return res   # возвращаю результат 
```

### 2 пункт


```python
def row_sums(matr):  
    if not matr:      # проверяю матрицу на пустоту 
        return []      # возвращаю пустой списк 
    row1 = len(matr[0])     
    for i in matr:            # проверка на рванность 
        if len(i) != row1:      
            return ValueError('Рванная матрица')
    sums = []              
    for rows in matr:      # прохожусь по строкам 
        row_sum = 0      # счетчик
        for element in rows:    # прохожусь по каждому значению строки 
            row_sum += element  # добавляю его в счетчик 
        sums.append(row_sum)   # добавляю в конечный список 
    return sums     # возвращаю результат 
```

### 3 пункт 


```python
def col_sums(matrix):
    if not matrix:
        return []              # проверка условий 
    row_first = len(matrix[0])    
    for r in matrix:
        if len(r) != row_first:
            return ValueError('рванная')
    num_cols = len(matrix[0])
    res = []
    for col_index in range(num_cols):      # тоже самое, что и в поиске суммы строки, только наоборот 
        col_sum = 0
        for r in matrix:
            col_sum += r[col_index]
        res.append(col_sum)
    return res
```

![Вывод_задача_B](/images/lab02/02.png)

## Задача C


```python
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        return TypeError('Не кортеж')
    if not isinstance(rec[2], float):
        return TypeError('Должен быть float')   
    if len(rec[0]) == 0 or len(rec[1]) == 0 or len(str(rec[2])) == 0:   # провекра на заполнение всех полей 
        return ValueError('Проверьте заполнение всех полей')
    lenal = str(rec[0]).split()     # удаляю лишние пробелы 
    if len(lenal) == 3:
        fio = str(rec[0]).title().strip()     # использую методы работы со строками 
        fio = fio.split()
        return f'{fio[0]} {fio[1][0]}. {fio[2][0]}., гр. {rec[1]}, GPA {rec[-1]:.2f}'
    elif len(lenal) == 2:
        fio = str(rec[0]).title().strip()
        fio = fio.split()                  # расматриваю случай, в котором ФИО записаны двумя словами 
        return f'{fio[0]} {fio[1][0]}, гр. {rec[1]}, GPA {rec[-1]:.2f}'
```

![Вывод_задача_C](/images/lab02/03.png)


# lab03

## задача А

### normalize
```python
normalize_test_case = [
 "ПрИвЕт\nМИр\t",      # "привет мир"
  "ёжик, Ёлка",        # "ежик, елка"
  "Hello\r\nWorld",    # "hello world"
  "  двойные   пробелы  "    # "двойные пробелы"
]


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    control_character = ['\n', '\t', '\r']
    for char in control_character:
        text = text.replace(char, ' ')   # если встречается один из символов, меняем его на пробел
    words = text.split() 
    text = ' '.join(words)    # убираем лишние пробелы

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')  # Замена ё на е

    if casefold:
        text = text.casefold()  # перевод в нижний регистр 
    
    return text

for i in normalize_test_case:
    print(f'"{i}" -> "{normalize(i)}"')     # вывод
```
## Вывод
![Вывод_normalize](/images/lab03/01.png)

### tokenize
```python
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
```
## Вывод
![Вывод_tokenize](/images/lab03/02.png)

### count_freq_top_n
```python
count_freq_and_top_n = [
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"],
]

def count_freg(tokens: list[str]) -> dict[str, int]:
    from collections import Counter
   
    return dict(Counter(tokens)) # считаем частоты элементов 

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    my_list = list(freq.items())

    def sort_po_alfavity(key_v):
        return key_v[0]
    my_list.sort(key=sort_po_alfavity)

    def sort_po_num(key_v):
        return key_v[1]
    my_list.sort(key=sort_po_num, reverse=True)

    return my_list[:n]


for tokens in count_freq_and_top_n:
    freq_dict = count_freg(tokens) 
    print(f"Частоты: {freq_dict}")
    print(f"Топ: {top_n(freq_dict)}")  
```

## Вывод
![вывод_count_freq_and_top_n](/images/lab03/03.png)


## Задание В


### text_stats
```python
from my_lib.text import tokenize, count_freg, top_n
import sys


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
```
## Вывод без таблицы

![Вывод_text_stats](/images/lab03/04.png)

## Вывод с таблицей

![Выыод_таблица](/images/lab03/05.png)

# lab04

## Задача А

```python
from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает текстовый файл и возвращает его содержимое как одну строку.

    По умолчанию используется кодировка UTF-8.
    При необходимости можно указать другую, например encoding="cp1251".
    '''
    path = Path(path)
    with path.open('r', encoding=encoding) as file:
        return file.read()  


def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создаёт родительские директории для указанного пути, если их нет.

    Полезно перед записью файла, чтобы избежать ошибки FileNotFoundError.
    '''
    path = Path(path)
    parent = path.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Создаёт или перезаписывает CSV-файл с разделителем ','.

    Если указан header, записывает его первой строкой.
    Проверяет, что все строки в 'rows' имеют одинаковую длину.
    '''
    if not rows:
        raise ValueError("Список строк 'rows' не может быть пустым.")

    row_lengths = {len(r) for r in rows}
    if len(row_lengths) > 1:
        raise ValueError("Все строки в 'rows' должны быть одинаковой длины.")

    ensure_parent_dir(path)

    path = Path(path)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        if header:
            writer.writerow(header)
        writer.writerows(rows)


input_path = Path("data/input.txt")

try:
    content = read_text(input_path, encoding="utf-8")
    print("Содержимое файла input.txt:\n", content)
except FileNotFoundError:
    print("Файл не найден!")
except UnicodeDecodeError:
    print("Ошибка кодировки! Попробуйте encoding='cp1251'.")


rows = [
    (1, 'Петя', 17),
    (2, 'Ваня', 18),
    (3, 'Егор', 17)
]
write_csv(rows, "output/users.csv", header=("ID", "Name", "Age"))

print("\n Файл 'output/users.csv' успешно создан!")


#write_csv([("word","count"),("test",3)], "data/check.csv")
```

## Вывод
![Вывод_задача_А](/images/lab04/01.png)

## csv файл
![Вывод_csv](/images/lab04/02.png)

## Задача В

```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from src.text import tokenize, count_freg, top_n, normalize
import csv
from pathlib import Path

table = True

def print_table(top: list[tuple]):
    """
    Выводит топ слов с их частотами в табличном формате.

    Форматирует таблицу с двумя столбцами: слово и частота.
    Ширина столбца "слово" подстраивается под максимальную длину слова из списка.

    """
    if not top:
        print('Нет слов для отображения')
        return
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
    input_path = Path('data/input.txt')     # путь к входному файлу 
    output_path = Path("data/report.csv")   # путь куда нужно сохранить отчёт

    if not input_path.exists():
        print(f"Файл {input_path} не найден!")
        sys.exit(1)

    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки при чтении {input_path}: {e}")
        sys.exit(1) # принудительно завершаем программу 

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freg(tokens)

    def sort_key(item):
        '''
        функция сортировки по частоте 
        '''
        word, count = item
        return (-count, word)

    sorted_items = sorted(freq.items(), key=sort_key)
     
     # создание папки и запись csv
    output_path.parent.mkdir(parents=True, exist_ok=True)  # создаём все недостающие папки
    with output_path.open("w", newline="", encoding="utf-8") as file: # открывает csv файл для записи
        writer = csv.writer(file) # создаёт объект, который умеет писать CSV-строки
        writer.writerow(["word", "count"]) # записывает заголовок таблицы.
        writer.writerows(sorted_items) # записывает все пары (слово, количество
    
    # статистика по тексту 
    total_words = sum(freq.values())
    unique_words = len(freq)
    top5 = top_n(freq, n=5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print(f"Топ: {top5}")

    if table:
        print("\nТаблица топ слов:")
        print_table(top5)

if __name__ == "__main__":
    main()
```
## Вывод 
![Вывод](/images/lab04/03.png)

## Отчет
![csv_отчет](/images/lab04/04.png)