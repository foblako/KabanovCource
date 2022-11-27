a = 51 * 7 ** 12 - 7 ** 3 - 22
s = 0
while a != 0:
    s += a % 7
    a //= 7

print(s)

# 70
