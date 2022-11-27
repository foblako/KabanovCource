for i in range(21, 30):
    x = i
    s = ''
    while x != 0:
        s += str(x % 3)
        x //= 3
    if s[0] == "1" and s[1] == "1":
        print(i)

# 22
