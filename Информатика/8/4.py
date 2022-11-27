from itertools import *

k = 0
w = product("ЛОДКА", repeat=4)
for i in w:
    if i.count("О") >= 2:
        k += 1

print(k)

# 113
