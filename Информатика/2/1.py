print("x w z y")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or not (y)) and not (y == z) and w
                if f:
                    print(x, w, z, y)
