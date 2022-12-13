def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    k = 0
    for i in divs:
        if i % 10 == 7:
            k +=1
    if k == 3:
        return sorted([i for i in divs if i % 10 == 7])
    return 0

for i in range(550000, 1000000):
    if div(i) != 0:
        print(i, div(i)[-1])