from fnmatch import *


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return d


for x in range(65001, 100000000):
    if fnmatch(str(x), "6*97*5?"):
        print(x, sum([i for i in div(x) if i % 2 == 0]), [i for i in div(x) if i % 2 == 0])
