k = 0
for i in range(1, 1000):
    b = bin(i)[2:]
    b += str(b.count("1") % 2)
    b += str(b.count("1") % 2)
    if int(b, 2) < 80:
        k += 1
print(k)

