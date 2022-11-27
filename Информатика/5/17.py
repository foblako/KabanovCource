for n in range(10, 10000):
    r = max([int(str(n)[i] + str(n)[i + 1]) for i in range(len(str(n)) - 1)]) - min(
        [int(str(n)[i] + str(n)[i + 1]) for i in range(len(str(n)) - 1)])
    if r == 44:
        print(n)
        break
