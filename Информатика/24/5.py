s = open("5.txt").readline()
s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")

f = set()
for i in s.split(" "):
    f.add(len(i))
print(max(f))
