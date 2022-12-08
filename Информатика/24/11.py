f = open("11.txt").readline()
f = f.replace("X", "1")
f = f.replace("Y", "2")
f = f.replace("Z", "3")

sub = f[0]
m = 0
for i in range(1, len(f)):
    if int(f[i]) >= int(f[i - 1]):
        sub += f[i]
        m = max(m, len(sub))
    else:
        sub = f[i]

print(m)
