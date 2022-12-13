def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def div(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sorted(divs)


for i in range(125697, 125722):
    d = [i for i in div(i) if prime(i)]
    if len(d) == 2 and d[0] * d[1] == i:
        print(d[0], d[1])

print(div(113000024))