from itertools import *

t = product("01234", repeat=6)
k = 0
for i in t:
    if i[0] != "0":
        if i[0] != "1" and i[-1] != "3" and i[-1] != "4":
            k += 1
print(k)

# 5625
