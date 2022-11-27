for x in range(1, 1000):
    b = bin(x)[2:]
    if x % 2 == 0:
        b += "01"
    else:
        b += "10"
    if int(b, 2) > 81:
        print(int(b, 2))
        break
