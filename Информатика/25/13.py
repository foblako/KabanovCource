def div(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    return sorted(divs)


for i in range(154026, 154044):
    if len(div(i)) == 4:
        print(div(i)[-2], div(i)[-1])
