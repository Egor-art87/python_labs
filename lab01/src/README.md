Задача 1
name = str(input('Введите ваше имя: ')).  # запросил имя
age = int(input('Введите ваш возраст: ')). # возраст
print(f'Привет {name}! Через год тебе будет {age+1}.') # сформировал вывод
![вывод_задача1](/lab01/src/images/01.png)
Задача 2
a = 3.5
b = 4.25
summ = a + b # ищем сумму
avg = (a + b) / 2 # находим avg
print(f'{summ:.2f} {avg:.2f}') # Формипуем вывод
![Вывод_задача2](/lab01/src/images/02.png)
Задача 3
price = 1000
discount = 10 
vat = 20 
base = price * (1 - discount/100) 
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скилки: {base:.2f}')
print(f'НДС: {vat_amount:.2f}')
print(f'Итого к оплате: {total:.2f}')
![Вывод_задача3](/lab01/src/images/03.png)
Задача 4
m = int(input('Введите минуты: '))
a = m // 60 
ost = m % 60
print(f'Митнуты: {m}')
print(f'{a}:{ost}')
![Вывод_задача4](/lab01/src/images/04.png)
Задача 5
fio = str(input('Введите своё ФИО: '))
fio_b = ' '.join(fio.split())
ini = str(input('Введите свои инициалы: ')).upper().strip()
print(f'ФИО: {fio_b}')
print(f'Инициалы: {ini}')
print(f'Длина: {len(fio_b) + len(ini)}')
![Вывод_задача5](/lab01/src/images/05.png)
Задача 6
n, o, z = int(input()), 0, 0
for i in range(n):
    a = input('in_' + str(i + 1) + ':').split()
    if (a[-1]) == 'True': o +=1
    elif (a[-1]) == 'False': z += 1
print(f'out: {o} {z}') 
![Вывод_задача5](/lab01/src/images/06.png)
Задача 7
s = input()
z = 'QWERTYUIOPASDFGHJKLZXCVBNM'
num = '1234567890'
s_r = ''
res_pos_num = []
for i in s:
    if i in z:
        s_r += i


for i in range(len(s) - 1):
    if s[i].isdigit():       # проверяю является ли текущий элемент цифрой 
        res_pos_num.append(s[i+1])
        break
s_r += ''.join(res_pos_num) # преобразовал и добавил список в строку
for i in range(len(s) - 1):
    if s[i].isdigit():
        x = s[i+1]     # Нашёл второй символ 
        break
for i in range(len(s) - 1):
    if s[i] == list(s_r)[0]:  # нашёл индекс первой буквы
        ind1 = i

for i in range(len(s) - 1):
    if s[i] == list(s_r)[1]:      # нашёл индекс второй буквы
        ind2 = i


step = ind2 - ind1    # считаю шаг между символами 


step_simvol = s[::-step][::-1]
for i in range(len(step_simvol) - 1):
    if step_simvol[i] == list(s_r)[1]:
        q = i-1
result = step_simvol[5:]
print(result)
![Вывод_задача5](/lab01/src/images/07.png)