f = [0]*100
for n in range(len(f)):
    if n == 1:
        f[n] = 2
    if n > 1:
        f[n] = f[n-1] + 5 * n ** 2
print(f[39])
