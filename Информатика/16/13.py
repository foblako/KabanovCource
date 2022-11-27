s = [0] * 1000
for n in range(len(s)):
    if n <= 10:
        s[n] = n
    if 10 <= n <= 36:
        s[n] = n // 4 + s[n - 10]
    if n > 36:
        s[n] = 2 * s[n - 5]
print(s[100])
