# Тест кейсы 
lst1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
lst2 = ("Петров Пётр", "IKBO-12", 5.0)
lst3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
lst4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
lst5 = ("", "IKBO-62-25", 3.55)
lst6 = ('артюх   егор ', 'БИВТ-25-7', 3.7)
lst7 = ("Петров Пётр Петрович", "IKBO-12", 78)
lst8 = ["Иванов Иван Иванович", "BIVT-25", 4.6]
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

print(format_record(lst1))
print(format_record(lst2))
print(format_record(lst3))
print(format_record(lst4))
print(format_record(lst5))
print(format_record(lst6))
print(format_record(lst7))
print(format_record(lst8))

    



