def f(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.update([i, x // i])
    k = 0
    for i in s:
        if i % 2 == 0:
            k += 1
    if k == 4:
        return sorted([i for i in s if i % 2 == 0])
    else:
        return 0


for i in range(190201, 190261):
    if f(i) != 0:
        print(f(i)[-1], f(i)[-2])
