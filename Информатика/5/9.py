for i in range(1, 10000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b = "1" + b + "0"
    else:
        b = b + "11"
    if int(b, 2) > 52:
        print(int(b, 2))
        break
