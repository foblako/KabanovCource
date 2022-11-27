k = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if x > 0 and y > (15 / 26) * x and y < 30 - (15 / 26) * x:
            k += 1
print(k)
