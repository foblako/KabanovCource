for x in range(1, 1000):
    b = bin(x)[2:]
    b += b[-1]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if int(b, 2) > 144:
        print(int(b, 2))
        break
