from itertools import *

k = set()
words = permutations("МИМИКРИЯ")
for w in words:
    k.add("".join(w))

print(len(k))

# 3360
