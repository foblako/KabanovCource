def f(x, y):
    if x > y: return 0
    if x == y: return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 2 + 1, y)


print(f(int('100', 2), int('11101', 2)))
