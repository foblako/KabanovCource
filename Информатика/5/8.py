for i in range(1, 1000):
    b = bin(2 * i)[2:]
    b += str(b.count("1") % 2)
    b += str(b.count("1") % 2)
    if int(b, 2) > 1017:
        print(i)
        break
