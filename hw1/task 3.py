# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите x (X ≠ 0) "))
y = int(input("Введите y (Y ≠ 0) "))

if x == 0:
    print("точка на оси икс")
if y == 0:
    print("точка на оси игрек")
if (x > 0 and y > 0):
    print("точка во 2ой четверти")
if (x > 0 and y < 0):
    print("точка во 3ей четверти")
if (x < 0 and y > 0):
    print("точка во 1ой четверти")
if (x < 0 and y < 0):
    print("точка во 4ой четверти")
