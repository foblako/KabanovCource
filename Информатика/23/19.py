d = set()


def f(x, k):
    if k == 15:
        d.add(x)
    else:
        f(x * 2, k + 1)
        f(x * 2 + 1, k + 1)


f(1, 0)
print(len(d))
