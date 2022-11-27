a = 3 * 16 ** 8 - 4 ** 5 + 3
s = ""
while a != 0:
    s += str(a % 4)
    a //= 4
print(s.count("3"))

# 12
