def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    r = 0
    for i in divs:
        if i % 3 == 0:
            r += 1
    if r == 5:
        return sorted([i for i in divs if i % 3 == 0])
    return 0

for i in range(300000,5000000):
    if div(i) != 0:
        print(i, div(i)[-1])
