s = open("3.txt").readline()
a = set()
k = 0
for i in range(len(s)):
    if s[i] != "D":
        k += 1
    else:
        a.add(k)
        k = 0
print(max(a))
