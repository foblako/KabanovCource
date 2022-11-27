def convert(a):
    s = []
    while a != 0:
        s.append(a % 12)
        a //= 12
    return s


print(convert(6 * 144 ** 26 + 11 * 12 ** 75 - 48).count(11))

# 51
