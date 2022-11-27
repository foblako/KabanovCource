print("w,z,y,x")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not w) and ((y or z) <= ((not x) and y))
                if f:
                    print(w,z,y,x)
