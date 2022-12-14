def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

for i in range(102, 112):
    if prime(i):
        print(i**4, i**3)