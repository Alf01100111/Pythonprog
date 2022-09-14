# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141

k = 1
pii = 0
for k in range(1, 1000000):
    pii = pii+4*((-1)**(k+1))/(2*k-1)
print(round(pii, 10))

d = 0.001


def num_after_dot(num :int) -> int:  #посчитаем сколько цифр оставим после запятой
    res = 0
    while num != 1:
        num *= 10
        res += 1
    return res

res = str(round(pii, num_after_dot(d)+1)) #округлим до нужной цифры + 1

print(res[0:len(res)-1]) #берем срез без последней неверно округленной цифры
