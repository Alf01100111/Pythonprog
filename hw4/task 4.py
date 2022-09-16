# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
z = 100
k = random.randint(1,z)
print(k)

res = ""
strr = ""
i = k
while i >= 0:
    
    if i != 0:
        strr = (f"{random.randint(1,z)}*x^{i}")
    else:
        strr = (f"{random.randint(1,z)}")

    
    if i != 0:
        res += strr + " + "
    else:
        res += strr + " = 0"

    i  -= 1

print(res)

with open('myfile.txt','w') as f:
    f.write(res)