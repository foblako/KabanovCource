def f(x, y, k):
    if x > y or k > 7: return 0
    if x == y and k != 7: return 0
    if x == y and k == 7: return 1
    if x < y:
        return f(x + 1, y, k + 1) + f(x * 2, y, k + 1) + f(x + 4, y, k + 1)


print(f(3, 27, 0))
