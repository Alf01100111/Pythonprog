# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]





a = [1, 2, 3, 2, 5, 1, 8, 8, 10, 15]

def non_repeat(a):
    cop1=list(a)
    b=list(set(a))
    for x in b:
        cop1.remove(x)
    for x in cop1:
        b.remove(x)
    return b

print(non_repeat(a))




# arr = [1, 1, 2, 3, 5, 5]  #не работает не знаю что не так
# unic = []


# for i in range(0,len(arr)):
#     is_unic = False

#     for j in range(0,len(arr)):
#         if (arr[i] != arr[j]) and i!=j:
#             is_unic == True

#     if is_unic == True:
#         unic.append(arr[i])

# print(unic)