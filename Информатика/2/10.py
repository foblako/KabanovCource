print("y,x,z,")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = not(x == (not y or z))
            print(y,x,z,f)
