print("x,y,w,z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x == (not (z))) <= ((x or w) == y)
                if not f:
                    print(x, y, w, z)
