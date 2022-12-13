def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    try: return sorted(divs)[-1] + sorted(divs)[0]
    except: return 0

for i in range(250200,100000000):
    if div(i) % 123 == 17:
        print(i, div(i))