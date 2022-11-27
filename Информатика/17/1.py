file = [int(i) for i in open("17.txt")]
a = []
for i in file:
    if i % 3 == 0 and i % 17 != 0 and i % 7 != 0 and i % 19 != 0 and i % 27 != 0:
        a.append(i)

print(len(a), max(a))