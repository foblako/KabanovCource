def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(81234, 134689):
    if len(div(x)) == 5:
        print(x, div(x))
