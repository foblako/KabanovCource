s = 0
for n in range(2,100000):
    a = n
    if a % 3 == 0:
        a //= 3
    else:
        a -= 1
    if a % 5 == 0:
        a //= 5
    else:
        a -= 1
    if a % 11 == 0:
        a //= 11
    else:
        a -= 1
    if a == 8:
        s += 1
print(s)