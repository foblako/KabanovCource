from fnmatch import *


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d


for x in range(0, 10000000, 3 * 7 * 8):
    if fnmatch(str(x), "?6*6*?6"):
        print(x, sum(div(x)))
