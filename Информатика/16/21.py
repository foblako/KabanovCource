f = [0] * 100
g = [0] * 100
for n in range(100):
    if n == 1:
        f[n] = g[n] = 1
    if n > 1:
        f[n] = f[n - 1] - 2 * g[n - 1]
        g[n] = f[n - 1] + g[n - 1] + n
print(sum([int(x) for x in str(g[36])]))
