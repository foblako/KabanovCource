def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a |= {i, x // i}
    return sum([i for i in a if i % 2 == 0])


for i in range(1204300, 1204381):
    if f(i) % 10 == 0 and f(i) != 0:
        print(i, f(i))
