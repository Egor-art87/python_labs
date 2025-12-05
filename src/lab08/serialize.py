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