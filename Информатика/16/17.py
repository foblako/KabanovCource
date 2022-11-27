f = [0] * 100
for n in range(len(f)):
    if n <= 3:
        f[n] = 3
    if n > 3 and n % 2 == 0:
        f[n] = f[n // 2] + 5
    if n > 3 and n % 2 != 0:
        f[n] = f[n - 1] - f[n - 2]
print(f[20])
