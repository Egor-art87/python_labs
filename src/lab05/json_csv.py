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

def main():
    data = [{"name": "Alice", "age": 22}, 
            {"name": "Bob", "age": 25}, 
            {"name": 'Egor', "age": 17}
            ]
    json_write(data)
    json_to_csv("data/out/people.json", "data/out/people.csv")
    csv_to_json("data/out/people.csv", "data/out/csv_to_json.json")

main()


    
    
    