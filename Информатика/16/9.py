import sys

sys.setrecursionlimit(10000000)


def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2 * f(n - 1)


print(f(1900) // 2 ** 1890)
