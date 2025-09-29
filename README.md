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

markdown
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

markdown
```python
print('unique_sorted')
print(list(sorted(dict.fromkeys(list6))))
print(list(sorted(dict.fromkeys(list7))))
print(list(sorted(dict.fromkeys(list8))))
print(list(sorted(dict.fromkeys(list9))))
```

### 3 пункт 

Создаю пустой список, прохожусь по элементом первоначального списка, если i является списком или кортежем, добавляю её в пустой список. Иначе - ошибка  

markdown
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

![Вывод_задача1](/images/lab02/01.png)

## Задача B
