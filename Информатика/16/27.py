def f(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        f(n - 1)
        f(n - 3)
        k += 1


k = 0
f(40)
print(k)
