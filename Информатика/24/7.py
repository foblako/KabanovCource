s = open("7.txt").readline()
s = s.replace("XY", "X Y")
s = s.replace("XZ", "X Z")
a = set()
for i in s.split():
    a.add(len(i))
print(max(a))
