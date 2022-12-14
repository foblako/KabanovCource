def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for i in range(113_000_000, 114_000_001):
    if i % 2 == 0 and i % 4 != 0:
        t = i // 2
        if int(t**0.5)**2 == t and prime(int(t**0.5)):
            print(i, int(t**0.5)*2)