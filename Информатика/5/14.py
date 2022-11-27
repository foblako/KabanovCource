for n in range(100, 1000):
    a1 = int(str(n)[0]) ** 2 + int(str(n)[1]) ** 2
    a2 = int(str(n)[1]) ** 2 + int(str(n)[2]) ** 2
    if int(max(str(a1), str(a2)) + min(str(a1), str(a2))) == 9010:
        print(n)
