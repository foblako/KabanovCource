import fnmatch

f = open("14.txt").readline()
f = f.replace("G", " ")
print(f)
m = 0
a = []
for i in f:
    m += 1
    if i == " ":
        a.append(m)
        m = 0

print(a)