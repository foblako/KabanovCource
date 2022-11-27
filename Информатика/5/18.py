ch = [0, 2, 4 ,6 ,8]
for n in range(2, 10000):
    s = [int(i) for i in str(n)]
    sch = sum([i for i in s if i in ch])
    schpos = sum([s[i] for i in range(len(s)) if i % 2 != 0])
    if abs(schpos - sch) == 9:
        print(n)
        break
