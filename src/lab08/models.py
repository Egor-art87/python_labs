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