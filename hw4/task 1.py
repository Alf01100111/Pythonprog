# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141


d = 0.001
pii = 3.1415926535

def num_after_dot(num :int) -> int:
    res = 0
    while num != 1:
        num *= 10
        res += 1
    return res

res = str(round(pii, num_after_dot(d)+1))

print(res[0:len(res)-1])
