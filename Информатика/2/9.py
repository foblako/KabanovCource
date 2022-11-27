print("z,w,y,x")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not y or x or z) and (not z or y)
                if not f:
                    print(z,w,y,x)
