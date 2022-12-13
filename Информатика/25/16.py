def div(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.update([i, x // i])
    try: return sum(divs)//len(divs)
    except: return 0

for i in range(550000, 10000000):
    if div(i) % 31 == 13:
        print(i, div(i))