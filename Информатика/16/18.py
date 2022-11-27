f = [0] * 100
for n in range(len(f)):
    if n == 1:
        f[n] = 1
    if n == 2:
        f[n] = 2
    if n > 2 and n % 2 == 0:
        f[n] = (n + f[n - 2]) // 5
    if n > 2 and n % 2 != 0:
        f[n] = (2 * n + f[n - 1] + f[n - 2]) // 4
print(f[50])
