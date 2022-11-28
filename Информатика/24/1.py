s = open("1.txt").readline()
a = set()
k = 0
for i in range(len(s)):
    if s[i] == "C":
        k += 1
    else:
        a.add(k)
        k = 0
print(max(a))
