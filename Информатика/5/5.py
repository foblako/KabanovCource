def c(h):
    s = ""
    while h != 0:
        s += str(h % 3)
        h //= 3

    return s[::-1]


for i in range(1000):
    i3 = c(i) + str(i % 3)
    print(int(i3, 3))
