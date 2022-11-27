k = 0
for y in range(-1000, 1000):
    for x in range(-1000, 1000):
        if y < x and y > -x and y > x - 55 * 2 ** 0.5 and y < -x + 55 * 2 ** 0.5:
            k += 1
print(k)
