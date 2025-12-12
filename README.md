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


# lab07


## test_text.py

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """Тест базовой нормализации"""
    text = "HeLlo WOrld"
    result = normalize(text)
    assert result == "hello world"


def test_normalize_control_chars():
    """Тест удаления управляющих символов"""
    text = "Hello\tWorld\nTest"
    result = normalize(text)
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result


def test_normalize_yo2e():
    """Тест замены ё на е"""
    text = "ёжик ёлка Ёлка Ёжик"
    result = normalize(text)
    assert result == "ежик елка елка ежик"


def test_normalize_empty_string():
    """Тест нормализации пустой строки"""
    assert normalize("") == ""


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", ""),
        ("Hello\tWorld", "hello world"),
        ("TEST", "test"),
    ],
)
def test_normalize_parametrized(text, expected):
    """Параметризованные тесты для normalize"""
    assert normalize(text) == expected


def test_tokenize_basic():
    """Тест базовой токенизации"""
    text = "hello world test"
    result = tokenize(text)
    assert result == ["hello", "world", "test"]


def test_tokenize_hyphens():
    """Тест токенизации с дефисами"""
    text = "hello-word hi-hyphen"
    result = tokenize(text)
    assert result == ["hello-word", "hi-hyphen"]


def test_tokenize_empty_string():
    """Тест токенизации пустой строки"""
    assert tokenize("") == []


def test_count_freq_basic():
    """Тест подсчета частот"""
    tokens = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "orange": 1}
    assert result == expected


def test_count_freq_empty_list():
    """Тест подсчета частот пустого списка"""
    assert count_freq([]) == {}


def test_count_freq_single_word():
    """Тест подсчета частот одного слова"""
    assert count_freq(["test"]) == {"test": 1}


def test_top_n_basic():
    """Тест получения топ-N слов"""
    freq = {"apple": 5, "banana": 3, "orange": 4, "grape": 2}
    result = top_n(freq, 3)
    assert len(result) == 3
    assert result[0][0] == "apple" and result[0][1] == 5
    assert result[1][0] == "orange" and result[1][1] == 4
    assert result[2][0] == "banana" and result[2][1] == 3


def test_top_n_same_frequency():
    """Тест одинаковых частот - сортировка по алфавиту"""
    freq = {"banana": 3, "apple": 3, "cherry": 3, "date": 2}
    result = top_n(freq, 3)
    assert result == [("apple", 3), ("banana", 3), ("cherry", 3)]
    assert result[0][0] == "apple"
    assert result[1][0] == "banana"
    assert result[2][0] == "cherry"


def test_top_n_more_than_available():
    """Тест когда запрашиваем больше элементов чем есть"""
    freq = {"apple": 3, "banana": 2}
    result = top_n(freq, 5)
    assert result == [("apple", 3), ("banana", 2)]


def test_top_n_zero_n():
    """Тест запроса 0 элементов"""
    freq = {"apple": 3, "banana": 2}
    assert top_n(freq, 0) == []


@pytest.mark.parametrize(
    "freq,n,expected",
    [
        ({}, 5, []),
        ({"a": 1}, 0, []),
        ({"a": 2, "b": 1}, 2, [("a", 2), ("b", 1)]),
        ({"b": 1, "a": 1}, 2, [("a", 1), ("b", 1)]),
    ],
)
def test_top_n_parametrized(freq, n, expected):
    """Параметризованные тесты для top_n"""
    assert top_n(freq, n) == expected
```

## Запуск тестов с покрытием:
![покрытие](/images/lab07/test_text_покрытие.png)


## test_json_csv.py

```python
import pytest
import json
import csv
import tempfile
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_correct_conversion(tmp_path):
    """Позитивный тест: корректная конвертация JSON → CSV"""
    # Создаем тестовый JSON файл
    json_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"}
    ]
    
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "output.csv"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    # Выполняем конвертацию
    json_to_csv(str(json_file), str(csv_file))
    
    # Проверяем что CSV файл создан
    assert csv_file.exists()
    
    # Проверяем содержимое CSV
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Проверяем количество записей
        assert len(rows) == 2
        
        # Проверяем набор ключей/заголовков
        expected_headers = ["name", "age", "city"]
        assert reader.fieldnames == expected_headers
        
        # Проверяем данные
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "30"
        assert rows[0]["city"] == "New York"


def test_csv_to_json_correct_conversion(tmp_path):
    """Позитивный тест: корректная конвертация CSV → JSON"""
    # Создаем тестовый CSV файл
    csv_data = [
        ["name", "age", "city"],
        ["Alice", "30", "New York"],
        ["Bob", "25", "London"]
    ]
    
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "output.json"
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    
    # Выполняем конвертацию
    csv_to_json(str(csv_file), str(json_file))
    
    # Проверяем что JSON файл создан
    assert json_file.exists()
    
    # Проверяем содержимое JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        # Проверяем количество записей
        assert len(data) == 2
        
        # Проверяем набор ключей/заголовков
        expected_keys = ["name", "age", "city"]
        assert list(data[0].keys()) == expected_keys
        
        # Проверяем данные
        assert data[0]["name"] == "Alice"
        assert data[0]["age"] == "30"
        assert data[0]["city"] == "New York"


def test_json_to_csv_file_not_found():
    """Негативный тест: несуществующий JSON файл → FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_json_to_csv_invalid_file(tmp_path):
    """Негативный тест: некорректный JSON файл → ValueError"""
    json_file = tmp_path / "test.json"
    
    # Создаем некорректный JSON
    json_file.write_text("{ invalid json }")
    
    with pytest.raises(ValueError):
        json_to_csv(str(json_file), "output.csv")


def test_csv_to_json_file_not_found():
    """Негативный тест: несуществующий CSV файл → FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_csv_to_json_invalid_file(tmp_path):
    """Негативный тест: пустой CSV файл → ValueError"""
    csv_file = tmp_path / "test.csv"
    
    # Создаем пустой файл
    csv_file.write_text("")
    
    with pytest.raises(ValueError):
        csv_to_json(str(csv_file), "output.json")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```
## Запуск тестов с покрытием
![json_csv_test](/images/lab07/test_json_csv.png)


# lab08

## models.py

```python
from dataclasses import dataclass
from datetime import datetime, date
import re

@dataclass
class Student:
    fio: str
    birthdate: str  
    group: str
    gpa: float
    
    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")
        
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        
        print(f"Предупреждение: проверьте своё ФИО '{self.fio}'")
    
        if not re.match(r'^[A-ZА-ЯЁ]{2,4}-\d{2}-\d{2}$', self.group.upper()):
            raise ValueError(
                f"Неверный формат группы: '{self.group}'. "
                f"Ожидается формат: БУКВЫ-ЦИФРЫ-ЦИФРЫ\n"
                f"Примеры допустимых групп:\n"
                f"  - БИВТ-25-07 (русские буквы)\n"
                f"  - SE-01-02 (английские буквы)\n"
                f"  - ИВТ-23-01 (русские, 3 буквы)\n"
                f"  - ABC-12-34 (английские, 3 буквы)\n"
                f"  - ABCD-56-78 (английские, 4 буквы)"
            )
        self.group = self.group.upper()

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - birth_date.year 
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age
    
    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            fio=data.get("fio", ""),
            birthdate=data.get("birthdate", ""),
            group=data.get("group", ""),
            gpa=data.get("gpa", 0.0)
        )
    
    def __str__(self) -> str:
        return (f"Студент: {self.fio}\n"
                f"Группа: {self.group}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n"
                f"Средний балл: {self.gpa}")


# Тестирование
if __name__ == "__main__":
    try:
        student = Student(
            fio='Артюх Егор Андреевич',
            birthdate='2008-01-02',
            group='ИВТ-25-07',
            gpa=4.5
        )
        
        print("=== Метод __str__ ===")
        print(student.__str__())  
        print()
        
        print("=== Метод to_dict() ===")
        student_dict = student.to_dict()
        print(student_dict)
        print()
        
        print("=== Метод from_dict() ===")
        new_student = Student.from_dict(student_dict)
        print(new_student)
        print()
        
        print("=== Метод age() ===")
        print(f"Возраст: {student.age()} лет")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
```
### Пример работы 
![models](/images/lab08/models.png)

## serialize.py

```python
import json
from pathlib import Path
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """Сохраняет список студентов в JSON файл"""
    if not isinstance(students, list):
        raise ValueError(f"Ожидается список студентов, получено: {type(students)}")
    
    if not students:
        raise ValueError("Список студентов пуст")
    
    for i, student in enumerate(students):
        if not isinstance(student, Student):
            raise ValueError(f"Элемент {i} не является объектом Student: {type(student)}")
    
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    data = [student.to_dict() for student in students]
    
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    """Загружает список студентов из JSON файла"""
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    
    with file_path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError(f"Ожидается список в JSON файле, получено: {type(data)}")
    
    students = []
    
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} не является словарем: {type(item)}")
        
        required_fields = ['fio', 'birthdate', 'group', 'gpa']
        missing_fields = [field for field in required_fields if field not in item]
        if missing_fields:
            raise ValueError(f"Отсутствуют обязательные поля: {missing_fields}")
        
        student = Student.from_dict(item)
        students.append(student)
    
    return students


# Тестирование модуля
if __name__ == "__main__":
    # Создаем папку, если её нет
    Path("data/lab08").mkdir(parents=True, exist_ok=True)
    
    input_path = "data/lab08/students_input.json"
    output_path = "data/lab08/students_output.json"
    
    # Загружаем студентов из входного файла
    try:
        students = students_from_json(input_path)
        
        # Сохраняем студентов в выходной файл
        students_to_json(students, output_path)
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        print(f"Создайте файл {input_path} со студентами")
    except Exception as e:
        print(f"Ошибка: {e}")
```

## Примеры работы

### консоль
![consol](/images/lab08/serialize.png)

### входной файл
![input](/images/lab08/students_input.png)

### выходной файл
![out](/images/lab08/students_output.png)


# lab09

## Code group.py
```python
import csv
from pathlib import Path
from typing import List
from models import Student


class Group:
    """Класс для работы с базой данных студентов в CSV формате"""
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы студентов
        
        Args:
            storage_path: путь к CSV файлу с данными студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Создает файл с заголовком, если он не существует"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self) -> List[dict]:
        """Читает все строки из CSV файла"""
        students_data = []
        
        if not self.path.exists():
            return students_data
            
        with open(self.path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students_data.append(row)
        
        return students_data
    
    def _write_all(self, data: List[dict]) -> None:
        """Записывает все данные в CSV файл"""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(data)
    
    def list(self) -> List[Student]:
        """Возвращает всех студентов в виде списка объектов Student"""
        students_data = self._read_all()
        students = []
        
        for item in students_data:
            try:
                # Преобразуем gpa из строки в float, если нужно
                if 'gpa' in item and isinstance(item['gpa'], str):
                    item['gpa'] = float(item['gpa'])
                
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, TypeError) as e:
                # Пропускаем некорректные записи
                print(f"Пропуск некорректной записи: {e}")
                continue
        
        return students
    
    def add(self, student: Student) -> None:
        """Добавляет нового студента в базу данных"""
        if not isinstance(student, Student):
            raise ValueError(f"Ожидается объект Student, получено: {type(student)}")
        
        students_data = self._read_all()
        
        # Проверяем, нет ли уже студента с таким ФИО
        for item in students_data:
            if item['fio'] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        # Добавляем нового студента
        students_data.append(student.to_dict())
        
        # Записываем обновленные данные
        self._write_all(students_data)
    
    def find(self, substr: str) -> List[Student]:
        """Ищет студентов по подстроке в ФИО"""
        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students
    
    def remove(self, fio: str) -> None:
        """Удаляет студента по ФИО"""
        students_data = self._read_all()
        initial_count = len(students_data)
        
        # Фильтруем, оставляя только студентов, чье ФИО не совпадает
        students_data = [item for item in students_data if item['fio'] != fio]
        
        if len(students_data) == initial_count:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(students_data)
    
    def update(self, fio: str, **fields) -> None:
        """Обновляет поля существующего студента"""
        if not fields:
            raise ValueError("Не указаны поля для обновления")
        
        students_data = self._read_all()
        updated = False
        
        for i, item in enumerate(students_data):
            if item['fio'] == fio:
                # Обновляем указанные поля
                for key, value in fields.items():
                    if key in item:
                        item[key] = value
                    else:
                        raise ValueError(f"Поле '{key}' не существует в записи студента")
                
                # Валидируем обновленные данные
                try:
                    # Преобразуем gpa из строки в float
                    if 'gpa' in item and isinstance(item['gpa'], str):
                        item['gpa'] = float(item['gpa'])
                    
                    student = Student.from_dict(item)
                    # Если валидация прошла успешно, сохраняем изменения
                    students_data[i] = student.to_dict()
                    updated = True
                except ValueError as e:
                    raise ValueError(f"Ошибка валидации при обновлении: {e}")
        
        if not updated:
            raise ValueError(f"Студент с ФИО '{fio}' не найден")
        
        self._write_all(students_data)


if __name__ == "__main__":
    print("=" * 60)
    print("База данных студентов в CSV формате")
    print("=" * 60)
    
    # Путь к файлу базы данных
    db_path = "data/lab09/students.csv"
    
    # Создаем объект Group
    print(f"1. Инициализация базы данных: {db_path}")
    group = Group(db_path)
    
    # Проверяем, пуста ли база данных
    current_students = group.list()
    
    # Данные для заполнения базы
    students_data = [
        {
            "fio": "Артюх Егор Андреевич",
            "birthdate": "2008-01-21",
            "group": "БИВТ-25-07",
            "gpa": 4.2
        },
        {
            "fio": "Иванов Иван Иванович",
            "birthdate": "2006-07-22",
            "group": "ИВТ-25-08",
            "gpa": 4.7
        },
        {
            "fio": "Новиков Денис Сергеевич",
            "birthdate": "2005-11-15",
            "group": "SE-02-03",
            "gpa": 3.8
        },
        {
            "fio": "Волкова Екатерина Дмитриевна",
            "birthdate": "2007-02-28",
            "group": "ABC-25-34",
            "gpa": 4.9
        }
    ]
    
    # Если база пуста, заполняем данными
    if len(current_students) == 0:
        for student_dict in students_data:
            try:
                student = Student.from_dict(student_dict)
                group.add(student)
            except ValueError as e:
                print(f"Ошибка при добавлении {student_dict['fio']}: {e}")
    else:
        print(f"\n3. База уже содержит данные. Пропускаем заполнение.")
    
    # 4. Вывод всех студентов (метод list())
    print("\n2. Вывод всех студентов (метод list()):")
    print("-" * 50)
    students = group.list()
    
    if not students:
        print("В базе данных нет студентов")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.fio}")
            print(f"   Группа: {student.group}")
            print(f"   Дата рождения: {student.birthdate} (Возраст: {student.age()} лет)")
            print(f"   Средний балл: {student.gpa}")
            print()
    
    # 5. Поиск студентов (метод find())
    print("\n3. Поиск студентов (метод find('Артюх')):")
    print("-" * 50)
    found_students = group.find("Артюх")
    if found_students:
        for student in found_students:
            print(f"Найден: {student.fio}, группа: {student.group}, GPA: {student.gpa}")
    else:
        print("Студенты не найдены")
    
    # 6. Обновление данных (метод update())
    print("\n4. Обновление данных студента (метод update()):")
    print("-" * 50)
    new_gpa = 4.5
    try:
        group.update("Артюх Егор Андреевич", gpa=new_gpa)
        print(f"GPA студента Артюх Егор Андреевич обновлен до {new_gpa}")
    except ValueError as e:
        print(f" Ошибка при обновлении: {e}")
    
    # 7. Удаление студента (метод remove())
    print("\n5. Удаление студента (метод remove):")
    print("-" * 50)
    delit_student = "Волкова Екатерина Дмитриевна"
    try:
        group.remove(delit_student)
        print(f"Студент {delit_student} адалён")
    except ValueError as e:
        print(f"Ошибка при удалении: {e}")
    
    # 8. Итоговый список студентов
    print("\n6. Итоговый список студентов после операций:")
    print("-" * 50)
    final_students = group.list()
    if final_students:
        for i, student in enumerate(final_students, 1):
            print(f"{i}. {student.fio} - {student.group} - GPA: {student.gpa}")
    else:
        print("В базе данных нет студентов")
    
    # 9. Статистика
    print("\n7. Статистика по группе:")
    print("-" * 50)
    if final_students:
        total_gpa = sum(s.gpa for s in final_students)
        avg_gpa = total_gpa / len(final_students)
        print(f"Количество студентов: {len(final_students)}")
        print(f"Средний GPA: {avg_gpa:.2f}")
        print(f"Минимальный GPA: {min(s.gpa for s in final_students)}")
        print(f"Максимальный GPA: {max(s.gpa for s in final_students)}")
        
        # Распределение по группам
        groups = {}
        for student in final_students:
            group_name = student.group
            groups[group_name] = groups.get(group_name, 0) + 1
        
        print(f"\nРаспределение по группам:")
        for group_name, count in sorted(groups.items()):
            print(f"  {group_name}: {count} студентов")
    else:
        print("В базе данных нет студентов")
    
    print("\n" + "=" * 70)
    print("Демонстрация работы завершена!")
    print(f"Данные сохранены в файле: {db_path}")
    
    # Проверяем содержимое файла
    if Path(db_path).exists():
        print(f"\nСодержимое файла {db_path}:")
        print("-" * 50)
        with open(db_path, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print(f"\nФайл {db_path} не существует!")
```
## csv-file:
![csv](/images/lab09/students.png)

## Вывод в консоле:
```txt
============================================================
База данных студентов в CSV формате
============================================================
1. Инициализация базы данных: data/lab09/students.csv

2. Вывод всех студентов (метод list()):
--------------------------------------------------
1. Артюх Егор Андреевич
   Группа: БИВТ-25-07
   Дата рождения: 2008-01-21 (Возраст: 17 лет)
   Средний балл: 4.2

2. Иванов Иван Иванович
   Группа: ИВТ-25-08
   Дата рождения: 2006-07-22 (Возраст: 19 лет)
   Средний балл: 4.7

3. Новиков Денис Сергеевич
   Группа: SE-02-03
   Дата рождения: 2005-11-15 (Возраст: 20 лет)
   Средний балл: 3.8

4. Волкова Екатерина Дмитриевна
   Группа: ABC-25-34
   Дата рождения: 2007-02-28 (Возраст: 18 лет)
   Средний балл: 4.9


3. Поиск студентов (метод find('Артюх')):
--------------------------------------------------
Найден: Артюх Егор Андреевич, группа: БИВТ-25-07, GPA: 4.2

4. Обновление данных студента (метод update()):
--------------------------------------------------
GPA студента Артюх Егор Андреевич обновлен до 4.5

5. Удаление студента (метод remove):
--------------------------------------------------
Студент Волкова Екатерина Дмитриевна адалён

6. Итоговый список студентов после операций:
--------------------------------------------------
1. Артюх Егор Андреевич - БИВТ-25-07 - GPA: 4.5
2. Иванов Иван Иванович - ИВТ-25-08 - GPA: 4.7
3. Новиков Денис Сергеевич - SE-02-03 - GPA: 3.8

7. Статистика по группе:
--------------------------------------------------
Количество студентов: 3
Средний GPA: 4.33
Минимальный GPA: 3.8
Максимальный GPA: 4.7

Распределение по группам:
  SE-02-03: 1 студентов
  БИВТ-25-07: 1 студентов
  ИВТ-25-08: 1 студентов

======================================================================
Демонстрация работы завершена!
Данные сохранены в файле: data/lab09/students.csv

Содержимое файла data/lab09/students.csv:
--------------------------------------------------
fio,birthdate,group,gpa
Артюх Егор Андреевич,2008-01-21,БИВТ-25-07,4.5
Иванов Иван Иванович,2006-07-22,ИВТ-25-08,4.7
Новиков Денис Сергеевич,2005-11-15,SE-02-03,3.8
```