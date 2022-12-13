def div(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sorted(divs)


for i in range(6080068, 6080177):
    if len(div(i)) == 2:
        print(i)
