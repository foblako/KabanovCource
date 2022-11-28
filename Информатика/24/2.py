s = open("2.txt").readline()

a = set()
k = 0

for i in range(len(s)):
    if s[i] == "A" or s[i] == "B" or s[i] == "E" or s[i] == "F":
        k += 1
    else:
        a.add(k)
        k = 0
print(max(a))
