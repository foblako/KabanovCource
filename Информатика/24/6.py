f = open("6.txt").readline()
a = set()
k = 0
for i in range(len(f)):
    if f[i] in "0123456789":
        k += 1
    else:
        a.add(k)
        k = 0
print(max(a))
