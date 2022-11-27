from itertools import *

k = 0
words = product("АГИЛМОРТ", repeat=4)

for w in words:
    k += 1
    if "".join(w)[-1] == "М" and "".join(w)[-2] == "И":
        print(k)

# 4053
