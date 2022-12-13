def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sum(divs)


for i in range(150000, 1000000000):
    if div(i) % 13 == 10:
        print(i, div(i))