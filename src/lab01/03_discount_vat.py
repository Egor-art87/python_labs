price = 1000
discount = 10 
vat = 20 
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скилки: {base:.2f}')
print(f'НДС: {vat_amount:.2f}')
print(f'Итого к оплате: {total:.2f}')