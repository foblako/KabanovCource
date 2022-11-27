d = set()


def f(x, k):
    if k == 8:
        if 1000 <= x <= 1024:
            d.add(x)
    else:
        f(x + 1, k + 1)
        f(x + 5, k + 1)
        f(x * 3, k + 1)

f(1,0)
print(len(d))

