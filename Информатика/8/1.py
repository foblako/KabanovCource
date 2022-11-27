from itertools import *

words = product("КРЕСЛО", repeat=4)
k = 0
for word in words:
    if word[0] != "О" and word[0] != "Е" and (word[-1] == "О" or word[-1] == "Е"):
        k += 1
print(k)

# 288
