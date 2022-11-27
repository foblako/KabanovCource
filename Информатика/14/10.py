def conver(a):
    s = ""
    while a != 0:
        s += str(a % 6)
        a //= 6
    return s


print(conver(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875).count("5") - conver(
    5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875).count("0"))

# 1182
