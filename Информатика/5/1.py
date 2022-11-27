for x in range(1000):
    b = bin(x)[2:]
    b += str(b.count("1") % 2)
    b += str(b.count("1") % 2)
    if int(b, 2) > 80:
        print(int(b, 2))
        break
