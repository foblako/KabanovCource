f = [0] * 100
for n in range(len(f)):
    if n <= 1:
        f[n] = 1
    if n > 1 and n % 2 == 0:
        f[n] = 3 * n + f[n - 1]
    if n > 1 and n % 2 != 0:
        f[n] = 2 * f[n-2]
print(f[31])
