print("y, w, x, z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not x or y and not z) or w
                if not f:
                    print(y, w, x, z)
