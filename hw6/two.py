# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers_list =[2, 3, 5, 9, 3]
print(sum(numbers_list[item] for item in range(1, len(numbers_list), 2)))

# def new_list (x):
#     _list = []
#     for i in range(x):
#         _list.append(int(input(f"Введите число {i + 1}: ")))
#     print(f"Ваш список: {_list}")    
#     return _list  