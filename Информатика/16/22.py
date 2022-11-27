f = [0] * 1000
for n in range(1000):
    if n == 0:
        f[n] = 1
    if n == 1:
        f[n] = 3
    if n > 1:
        f[n] = f[n - 1] - f[n - 2] + 3 * n
print(f[40])
