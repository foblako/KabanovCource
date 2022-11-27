from itertools import *

k = 0
words = product("ВИШНЯ", repeat=6)

for w in words:
    if w.count("В") <= 1:
        if w[0] != "Ш" and w[-1] != "И" and w[-1] != "Я":
            k += 1

print(k)

# 4352
