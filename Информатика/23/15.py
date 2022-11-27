def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if str(x).count("9") == 0:
        return f(x + 11, y) + f(x + 1, y)
    else:
        return f(x + 10, y) + f(x + 1, y)


print(f(25, 51))
