# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def randlist(length, rnd) -> list:
    newlist = []
    for i in range(length):
        newlist.append(random.randrange(0, rnd))
    return newlist


def find_sum_on_even(arr,sum = 0) -> int:    
    for i in range(1,len(arr),2):
        sum += arr[i]
    return sum

array = randlist(10, 10)
print(array)
print(f"Сумма чисел на нечетных позициях {find_sum_on_even(array)}")