# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11


number = input("Введите вещественное число ")

array = list(number)
res = 0

for i in range(len(array)):
    if array[i].isdigit() == True:
        res += int(array[i])

print(f"Сумма цифр в числе {number} = {res}")