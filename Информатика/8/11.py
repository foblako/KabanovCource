from itertools import *

words = product("ABCD", repeat=4)
t = set()
for w in words:
    t.add("".join(sorted(w)))
print(len(t))

# 35
