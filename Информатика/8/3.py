from itertools import *

words = product("ПУЛЯ", repeat=6)
k = 0
for word in words:
    if word.count("У") == 2:
        k += 1

print(k)

# 1215
