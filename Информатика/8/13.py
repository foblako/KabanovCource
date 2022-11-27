from itertools import *

ch = product("123456789", repeat=3)
t = set()

for k in ch:
    t.add("".join(sorted(k)))

print(len(t))

# 165
