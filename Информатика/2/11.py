print("w,z,x,y")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= x) or not ((x <= z) and (z <= x)) and not w
                if not f:
                    print(w,z,x,y)
