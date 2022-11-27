from itertools import *

k = 0
words = product("САЛО", repeat=6)
for word in words:
    if 0 < word.count("О") <= 3:
        k += 1
print(k)

# 3213
