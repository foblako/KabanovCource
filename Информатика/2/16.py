print("z,x,w,y")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not (z and (not (w)))) or ((z <= w) == (x <= y))
                if not f:
                    print(z,x,w,y)
