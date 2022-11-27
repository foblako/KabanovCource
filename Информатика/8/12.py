from itertools import *

words = product("ГЕПАРД", repeat=5)
k = 0
for w in words:
    if w[0] != "А" and w[-1] != "Е" and "".join(w).count("Г") == 1:
        k += 1

print(k)

# 2200
