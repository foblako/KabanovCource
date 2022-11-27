import math

ch = [2, 4, 6, 8]
nch = [1, 3, 5, 7, 9]
for n in range(1, 1000):
    for m in range(1, 1000):
        p1 = math.prod([int(i) for i in list(str(n)) if int(i) in ch]) * math.prod(
            [int(i) for i in list(str(m)) if int(i) in ch])
        p2 = math.prod([int(i) for i in list(str(n)) if int(i) in nch]) * math.prod(
            [int(i) for i in list(str(m)) if int(i) in nch])
        if abs(p1 - p2) == 29 and n == 120:
            print(m)
            break
