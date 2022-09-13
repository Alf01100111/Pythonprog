# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(size: int) -> list:
    
    right = [1, 1]
    if size == 1:
        right =[1]
        
    for i in range(2, size):
        right.append(right[i-1] + right[i-2])  

    left = right.copy()
    for i in range(1, len(left), 2):
        left[i] *= -1
    left.reverse()

    return left + [0] + right

k = int(input('Введите k: '))
print(fib(k))