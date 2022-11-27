from itertools import *

k = 0
words = permutations("ИГРОК")
for word in words:
    if "".join(word).count("РОК") == 0 and word[0] != "К":
        k += 1
print(k)

# 90
