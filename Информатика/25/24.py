import sys


def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sorted(divs)


pr = [i for i in range(2, 1000) if len(div(i)) == 0]
for i in range(25317, 51238):
    k = 0
    a = [i]
    for j in div(i):
        if j in pr:
            k += 1
            a.append(j)
    if k >= 6:
        print(a[0], a[-1])
