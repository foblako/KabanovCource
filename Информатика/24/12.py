f = open("12.txt").readline()
sub = f[0]
m = 0
for i in range(1, len(f)):
    if f[i] > f[i - 1]:
        sub += f[i]
        m = max(m, len(sub))
    else:
        sub = f[i]

print(m)
