from itertools import *

k = 0
words = permutations("ВАЙФУ", 4)

for word in words:
    if word[0] != "Й" and "ВФ" not in "".join(word) and "ФВ" not in "".join(word):
        k += 1
print(k)

# 68
