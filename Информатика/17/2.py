file = [int(x) for x in open("17.txt")]
a = []
for i in file:
    if (i % 10 == 2 or i % 10 == 7) and (i % 3 ==0 and i % 11 == 0):
        a.append(i)

print(len(a), min(a))
