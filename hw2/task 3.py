# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
import math
import array

k = int(input("Введите К "))

array = []
sum = 0

for i in range(1,k+1):
    array.append((1+1/i)**i)
    sum += array[i-1]

print(array)
print(round(sum,3))
