def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n // 2) + 1
    if n >= 2 and n % 2 != 0:
        return n + f(n - 1)


for n in range(1, 501):
    if f(n) == 19:
        print(n)
        break
