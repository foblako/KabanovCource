k = 0
for y in range(1000):
    for x in range(1000):
        if y < 3 * x and y < 15 and y > (x / 4 - 14) and y > 0:
            k += 1
print(k)
