def convert(a):
    s = 0
    while a != 0:
        s += a % 6
        a //= 6
    return s


for x in range(10000):
    if convert(36 ** 17 - 6 ** x + 71) == 61:
        print(x)

# 24
