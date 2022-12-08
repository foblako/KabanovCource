f = open("13.txt").readline()
sub = m = f[0]
for i in range(1, len(f)):
    if f[i] < f[i - 1]:
        sub += f[i]
        m = max(m, sub, key=len)
    else:
        sub = f[i]
print(m)
