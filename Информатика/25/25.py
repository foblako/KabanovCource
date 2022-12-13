def primes(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sorted(divs)


for i in range(500000, 499000, -1):
    d = [i for i in div(i) if primes(i)]
    s = sum(d)
    if s != 0 and s % 10 == 0:
        print(i, s)
