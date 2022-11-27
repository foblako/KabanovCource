for n in range(2, 20000):
    b = bin(n)[2:]
    c1 = 0
    n0 = 0
    for i in range(1, len(b) + 1):
        if i % 2 == 0 and b[i - 1] == "1":
            c1 += 1
        elif i % 2 != 0 and b[i - 1] == "0":
            n0 += 1
    if abs(c1 - n0) == 5:
        print(n, abs(c1 - n0))
        break

