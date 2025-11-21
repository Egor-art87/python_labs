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

# lab05

## Задача А

### json_to_csv
```python
import json
import csv
from pathlib import Path


def json_write(data: list[dict]):
    '''
    Записываем JSON-файл
    '''
    path = Path("data/out/people.json")
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
 


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f'Файл {json_file} отсуствует')
    if json_file.suffix.lower() != '.json':
        raise ValueError(f'Файл {json_file} не json')
    
    try:
        with json_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f'неправильный кодировка json: {e}')
    
    if not isinstance(data, list):
        raise ValueError('json должен быть списком')
    if len(data) == 0:
        raise ValueError('Список не может быть = 0!')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError('Все элементы в списке должны быть словарями')
    

    csv_file = Path(csv_path)
    if csv_file.suffix.lower() != '.csv':
        raise ValueError('Файл должен быть csv')
    

    csv_file.parent.mkdir(parents=True, exist_ok=True)

    # формирование заголовка
    all_columns = set()
    for item in data:
        all_columns.update(item.keys())

    first_item_columns = list(data[0].keys()) if data else []
    additional_columns = sorted(all_columns - set(first_item_columns))
    columns = first_item_columns + additional_columns

    
    with csv_file.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)

        for item in data:
            row = []
            for column in columns:
                value = item.get(column, '')
                row.append(str(value))
            writer.writerow(row)
```
## Вход
![input](/images/lab05/json_to_csv_вход.png)

## Выход
![out](/images/lab05/json_to_csv_выход.png)

 ```python
 def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV фвйл {csv_path} не существует")
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"фходной файл должен быть csv {csv_file.suffix}")
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            if reader.fieldnames is None:
                raise ValueError("CSV-файл должен иметь заголовок")
            
            data = list(reader)
            
    except csv.Error as e:
        raise ValueError(f"Invalid CSV format: {e}")
    
    if len(data) == 0:
        raise ValueError("CSV-файл пустой")
    
    json_file = Path(json_path)
    if json_file.suffix.lower() != '.json':
        raise ValueError(f"Output file must be JSON, got {json_file.suffix}")
    
    json_file.parent.mkdir(parents=True, exist_ok=True)

    with json_file.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
 ```
 ## Вход
 ![Вход](/images/lab05/json_to_csv_выход.png)

 ## Выход
 ![out](/images/lab05/csv_to_json.png)

### Запуск кода
 ```python
def main():
    data = [{"name": "Alice", "age": 22}, 
            {"name": "Bob", "age": 25}, 
            {"name": 'Egor', "age": 17}
            ]
    json_write(data)
    json_to_csv("data/out/people.json", "data/out/people.csv")
    csv_to_json("data/out/people.csv", "data/out/csv_to_json.json")

main()
 ```

 ## Задание В

 ## csv_xlsx

 ```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)

    if not csv_file.exists():
        raise FileNotFoundError(f'Файл {csv_file} не найден')
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f'Файл {csv_file} не csv')
    
    xlsx_file = Path(xlsx_path)
    if xlsx_file.suffix.lower() != '.xlsx':
        raise ValueError(f'Файл {xlsx_file} не xlsx')
    
    try:
        with csv_file.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)

    except csv.Error as e:
        raise ValueError(f"Invalid CSV format: {e}")
    except UnicodeDecodeError:
        raise ValueError("кодировка должна быть UTF-8")
    
    if len(rows) == 0:
        raise ValueError('csv-файл пустой')
    
    if not rows[0] or all(cell.strip() == '' for cell in rows[0]):
        raise ValueError("CSV-файл должен иметь заголовок")
    
    xlsx_file.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook() # создает новый Excel файл
    ws = wb.active   # получает активный лист (по умолчанию первый)
    ws.title = 'lst1'

    # запись данных в ячейки
    for row_idx, row in enumerate(rows, 1):
        for col_idx, value in enumerate(row, 1):
            ws.cell(row=row_idx, column=col_idx, value=value)

    for column_cells in ws.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        adjusted_width = max(length + 2, 8)  
        column_letter = get_column_letter(column_cells[0].column)
        ws.column_dimensions[column_letter].width = adjusted_width

    wb.save(xlsx_path)

csv_to_xlsx('data/out/people.csv', 'data/out/csv_to_xlsx.xlsx')
 ```

## Вход
![input](/images/lab05/json_to_csv_выход.png)

## Выход
![out](/images/lab05/csv_to_xlsx.png)

# lab06

## cli_text

### КОД
```python
import argparse
import sys
from pathlib import Path
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from src.text import tokenize, normalize, top_n, count_freg


def run_cat(path: Path, out: Path | None = None, number_lines: bool = False):
    """Вывод содержимого файла с опциональной нумерацией строк."""
    if not path.exists():
        print(f"Ошибка: файл '{path}' не найден!", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{path}' не в UTF-8!", file=sys.stderr)
        sys.exit(1)

    lines = text.splitlines()

    if number_lines:
        output = "\n".join(f"{i+1:>4}  {line}" for i, line in enumerate(lines))
    else:
        output = "\n".join(lines)

    if out:
        out.write_text(output, encoding="utf-8")
    else:
        print(output)


def run_stats(path: Path, top: int = 10, out: Path | None = None):
    """Анализ частоты слов в файле."""
    if not path.exists():
        print(f"Ошибка: файл '{path}' не найден!", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{path}' не в UTF-8!", file=sys.stderr)
        sys.exit(1)

    tokens = tokenize(text)

    normalized = [normalize(token) for token in tokens]
    normalized = [t for t in normalized if t]  

    freq = count_freg(normalized)

    top_words = top_n(freq, top)

    if not top_words:
        print('Нет слов для отображения')
        return
    max_len = max(len(word) for word, _ in top_words)
    col_word = 'слово'
    col_freq = 'частота'

    width_word = max(max_len, len(col_word))
    width_freq = len(col_freq)
    print(f"{col_word:<{width_word}} | {col_freq}")
    print("-" * width_word + "-+-" + "-" * width_freq)

    for word, count in top_words:
        print(f"{word:<{width_word}} | {count}")


def build_parser():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_p = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("path", type=Path, help="Путь к файлу")
    cat_p.add_argument("-o", "--out", type=Path, help="Файл для вывода результата")
    cat_p.add_argument("-n", "--number", action="store_true", help="Нумеровать строки")

    stats_p = subparsers.add_parser("stats", help="Статистика слов")
    stats_p.add_argument("path", type=Path, help="Путь к файлу")
    stats_p.add_argument("-k", "--top", type=int, default=10, help="Топ N слов")
    stats_p.add_argument("-o", "--out", type=Path, help="Файл для вывода результата")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "cat":
        run_cat(args.path, args.out, args.number)

    elif args.command == "stats":
        run_stats(args.path, args.top, args.out)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```
## Работа cli_text
### Общая справка по cli_text
![общая_справка](/images/lab06/Первый_модуль_общая_справка.png)
### Справка по cat
![Спр_cat](/images/lab06/Справка_по_cat.png)
### Справка по stats
![stats](/images/lab06/справка_по_stats.png)
### Вывод cat
![cat](/images/lab06/Первый_модуль_нумерация_строк.png)
### Нумерация с сохранением в другой файл
![сохр_cat](/images/lab06/сохранение_в_файл_с_нумерацией_cat.png)
### Работа stats TOP
![stats_work](/images/lab06/Топ_из_всех_слов.png)
### TOP-5
![t-5](/images/lab06/Топ_5.png)


## cli_convert

```python
import argparse
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)

    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```
## Работа cli_convert

### Справка по Cli_convert
![справка_convert](/images/lab06/Справка_по_коевектору.png)

### json -> csv
![k](/images/lab06/json2csv_команда.png)![v](/images/lab06/json2csv_вывод.png)

### csv -> xlsx
![k](/images/lab06/csv2xlsx_команда.png)![v](/images/lab06/csv2xlsx_вывод.png)

### csv -> json
![k](/images/lab06/csv2json_команда.png)![v](/images/lab06/csv2json_вывод.png)