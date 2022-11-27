from itertools import *

k = 0
words = product("ЕЛМРУ", repeat=4)
for w in words:
    k += 1
    if w[0] == "Л":
        print(k)
        break

# 126
