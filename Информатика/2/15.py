print("c, a, d, b")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a and b) == (not (c))) and (b <= d)
                if f:
                    print(c, a, d, b)
