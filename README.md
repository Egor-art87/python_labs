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
print(list(sorted(dict.fromkeys(list6))))
print(list(sorted(dict.fromkeys(list7))))
print(list(sorted(dict.fromkeys(list8))))
print(list(sorted(dict.fromkeys(list9))))
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
ef row_sums(matr):  
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
        return f'{fio[0]} {fio[1][0]}, гр. {x[1]}, GPA {x[-1]:.2f}' # возвращаю результат 
```

![Вывод_задача_C](/images/lab02/03.png)