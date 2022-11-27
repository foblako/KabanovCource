k = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if y < 3 * x and y < 90 and y > x:
            k += 1
print(k)
