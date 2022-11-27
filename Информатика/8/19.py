from itertools import *

k = 0
words = product("АИМРЯ", repeat=4)

for w in words:
    k += 1
    if "".join(w) == "АРИЯ":
        print(k)
        break

# 85
