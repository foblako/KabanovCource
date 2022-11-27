from fnmatch import *


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(10 ** 7, 0, -1):
    if fnmatch(str(x), "9?*55*7"):
        print(x, sum([k for k in div(x)]) % 21)
