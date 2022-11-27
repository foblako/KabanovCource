from itertools import *

sg = ["ЙД", "ЙК", "ЙС", "ЙТ", "ЙР"]

words = permutations("ДЕЙКСТРА", 6)

k = 0

for word in words:
    if "".join(word).count("Й") == 1:
        for i in sg:
            if i in "".join(word):
                k += 1

print(k)

# 9000
