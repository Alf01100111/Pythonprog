# Реализуйте алгоритм перемешивания списка.
import random

array = []

for i in range(10):
    array.append(i)

print(array)

while True:
    choice = input("перемешать массив y/n ")
    if choice == 'y':
        i = len(array) - 1
        while i >= 1:
            j = random.randrange(0, i+1)
            tmp = array[j]
            array[j] = array[i]
            array[i] = tmp

            i-=1
        print(array)
    else: break