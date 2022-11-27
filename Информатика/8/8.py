from itertools import product

codes = product("AB123", repeat=8)
k = 0
for code in codes:
    s = "".join(code)
    if (s.count("A") == 1 and s.count("B") == 1) or (s.count("A") == 2 and s.count("B") == 0) or (
            s.count("A") == 0 and s.count("B") == 2):
        k += 1

print(k)

# 81648
