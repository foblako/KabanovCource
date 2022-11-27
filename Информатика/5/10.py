for i in range(1, 10000):
    b = bin(i)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    if int(b, 2) < 35:
        print(i)
