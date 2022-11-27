c = 0
for n in range(300, 401):
    s = {int(str(n)[0] + str(n)[1]), int(str(n)[0] + str(n)[2]), int(str(n)[1] + str(n)[2]), int(str(n)[1] + str(n)[0]),
          int(str(n)[2] + str(n)[0]), int(str(n)[2] + str(n)[1])}
    ms = max([i for i in s if i > 9])
    mis = min([i for i in s if i > 9])
    if ms - mis == 20:
        c += 1
print(c)
