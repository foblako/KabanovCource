f = [0] * 100
for n in range(len(f)):
    if n <= 1:
        f[n] = 0
    if n > 1 and n % 2 != 0:
        f[n] = f[n - 1] + 3 * n ** 2
    if n > 1 and n % 2 == 0:
        f[n] = n // 2 + f[n - 1] + 2
print(f[49])
