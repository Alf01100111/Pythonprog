# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


import math

factorial = int (input("Введите число: "))
print([math.factorial(i) for i in range(1,factorial +1)])

# factorial = int (input("Введите число: "))
# product = 1
# for i in range (1,factorial + 1) :
#     product *= i
#     print (product ,end = "  " )