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