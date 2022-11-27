for n in range(100, 1000):
    a1 = str(n)[0]
    a2 = str(n)[1]
    a3 = str(n)[2]

    w = [int(a1 + a2), int(a2 + a3), int(a3 + a1), int(a2 + a1), int(a3 + a2), int(a1 + a3)]
    for i in w:
        if i < 10:
            w.remove(i)
    if max(w) - min(w) == 5:
        print(n)
        break
