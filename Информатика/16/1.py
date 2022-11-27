import sys

sys.setrecursionlimit(1000000)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


print(f(2023) / f(2020))
