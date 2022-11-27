for n in range(100, 1000):
    a1 = int(str(n)[0]) * int(str(n)[1])
    a2 = int(str(n)[1]) * int(str(n)[2])
    if int(max(str(a1), str(a2)) + min(str(a1), str(a2))) == 240:
        print(n)
