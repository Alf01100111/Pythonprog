# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def randlistreal(length, rnd) -> list:
    newlist = []
    for i in range(length):
        newlist.append(random.randrange(0, rnd)/100)
    return newlist


def fract_part(num) -> float:
    return (num*100) % 100


def max_min_res(listt) -> float:

    maxx = fract_part(listt[0])
    minn = fract_part(listt[0])

    for i in range(len(listt)):
        if fract_part(listt[i]) > maxx:
            maxx = fract_part(listt[i])

        if fract_part(listt[i]) < minn:
            minn = fract_part(listt[i])

    return round((maxx - minn)/100, 2)


arr = randlistreal(5, 1000)
print(f"{arr} => {max_min_res(arr)}")
