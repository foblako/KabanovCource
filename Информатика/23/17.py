def f(x, y):
    if x > y: return 0
    if x == y: return 1
    return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)


for i in range(31, 80):
    if f(31, i) == 1001:
        print(i)
