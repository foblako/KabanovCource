def f(x, a):
    return ((x % 4 != 3) or (x % 6 != 1)) <= (x % 36 != a)


for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 10000)):
        print(a)
