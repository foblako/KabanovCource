f = [0] * 100
for n in range(len(f)):
    if n < 5:
        f[n] = 1 + 2 * n
    if n >= 5 and n % 3 == 0:
        f[n] = 2 * (n + 1) * f[n - 2]
    if n >= 5 and n % 3 != 0:
        f[n] = 2 * n + 1 + f[n - 1] + 2 * f[n - 2]
print(f[15])
