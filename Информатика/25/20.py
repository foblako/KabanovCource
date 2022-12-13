def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a |= {i, x // i}
    s = [i for i in a if i % 10 == 8 and i != 8]
    return [sum([i for i in a if i % 2 == 0]), s]


for i in range(500000, 1000000):
    if f(i)[1] != []:
        print(i, min(f(i)[1]))
