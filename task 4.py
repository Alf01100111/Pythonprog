# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random

n = int(input("Введите число N "))
array = []
for i in range(n*2):
    array.append(random.randrange(-n, n))

print(array)

pos = input("Введите номер двух элементов через пробел ")
list_of_pos = pos.split(' ')
x = array[int(list_of_pos[0])]
y = array[int(list_of_pos[1])]

print(f'произведение {x} и {y} = {x*y}') #можно вписать прям сюда array[int(list_of_pos[0])]*array[int(list_of_pos[1])] но помоему это уже не читабельно