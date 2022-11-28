s = open("10.txt").readline()
sub = s[0]
m = 0
for i in range(len(s) - 1):
    if s[i] != s[i - 1]:
        sub += s[i]
        m = max(len(sub), m)
    else:
        sub = s[i]
print(m)
