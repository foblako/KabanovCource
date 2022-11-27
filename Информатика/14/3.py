a = 2 * 27 ** 7 + 3 ** 10 - 9
s = ""
while a != 0:
    s += str(a % 3)
    a //= 3

print(s.count("0"))

# 13
