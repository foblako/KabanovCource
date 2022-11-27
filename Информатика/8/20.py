from itertools import *

k = 0
words = product("АИМРЯ", repeat=4)

for w in words:
    k += 1
    if k == 211:
        print("".join(w))

# ИРМА
