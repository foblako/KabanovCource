def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


pr = []
for x in range(174457, 174506):
    if len(f(x)) == 4:
        pr.append([f(x)[1] * f(x)[2] % 1000, f(x)[1], f(x)[2]])
print(sorted(pr))
