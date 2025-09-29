# Тест кейсы 
lst1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
lst2 = ("Петров Пётр", "IKBO-12", 5.0)
lst3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
lst4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
lst5 = ("", "IKBO-62-25", 3.55)
def string(x):
    if len(x[0]) == 0 or len(x[1]) == 0 or len(str(x[2])) == 0:   # провекра на заполнение всех полей 
        return ValueError('Проверьте заполнение всех полей')
    lenal = str(x[0]).split()     # удаляю лишние пробелы 
    if len(lenal) > 2:
        fio = str(x[0]).title().strip()     # использую методы работы со строками 
        fio = fio.split()
        return f'{fio[0]} {fio[1][0]}. {fio[2][0]}., гр. {x[1]}, GPA {x[-1]:.2f}'
    else:
        fio = str(x[0]).title().strip()
        fio = fio.split()                  # расматриваю случай, в котором ФИО записаны двумя словами 
        return f'{fio[0]} {fio[1][0]}, гр. {x[1]}, GPA {x[-1]:.2f}'

print(string(lst1))
print(string(lst2))
print(string(lst3))   
print(string(lst4))   
print(string(lst5))   

    



