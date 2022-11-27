def convert(a):
    s = ""
    while a != 0:
        s += str(a % 5)
        a //= 5
    return s


for x in range(1000):
    a = 125 ** 200 - 5 ** x + 74
    b = convert(a)
    if b.count("4") == 100:
        print(x)

# 502
