import operator


def f(x):
    a = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            a.update([i, x // i])
    r = 1
    a = sorted(list(a))
    try:
        for i in range(5):
            r *= a[i]
        return [r, a[4]]
    except:
        return 0


for i in range(400000000, 100000000000):
    try:
        if f(i)[0] % 100 == 17 and f(i)[0] < i:
            print(f(i)[0], f(i)[1])
    except:
        ...
