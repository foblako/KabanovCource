f = open("9.txt").readline()
while "XZZY" in f: f = f.replace("XZZY", "XZZ ZZY")
print(max([len(i) for i in f.split()]))
