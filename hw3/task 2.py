# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math


def randlist(length, rnd) -> list:
    newlist = []
    for i in range(length):
        newlist.append(random.randrange(0, rnd))
    return newlist


def find_mult_couple(arr, res_arr=[]) -> list:
    for i in range(math.ceil((len(arr)/2))):
        res_arr.append(arr[i] * arr[0 - (i+1)])
    return res_arr


array = randlist(5, 10)
print(f"{array} => {find_mult_couple(array)}")
