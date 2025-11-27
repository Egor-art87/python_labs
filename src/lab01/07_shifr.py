s = input()
z = "QWERTYUIOPASDFGHJKLZXCVBNM"
num = "1234567890"
s_r = ""
res_pos_num = []
for i in s:
    if i in z:
        s_r += i


for i in range(len(s) - 1):
    if s[i].isdigit():  # проверяю является ли текущий элемент цифрой
        res_pos_num.append(s[i + 1])
        break
s_r += "".join(res_pos_num)  # преобразовал и добавил список в строку
for i in range(len(s) - 1):
    if s[i].isdigit():
        x = s[i + 1]  # Нашёл второй символ
        break
for i in range(len(s) - 1):
    if s[i] == list(s_r)[0]:  # нашёл индекс первой буквы
        ind1 = i

for i in range(len(s) - 1):
    if s[i] == list(s_r)[1]:  # нашёл индекс второй буквы
        ind2 = i


step = ind2 - ind1  # считаю шаг между символами


step_simvol = s[::-step][::-1]
for i in range(len(step_simvol) - 1):
    if step_simvol[i] == list(s_r)[1]:
        q = i - 1
result = step_simvol[5:]
print(result)
