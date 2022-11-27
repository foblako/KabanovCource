file = [int(x) for x in open("17_8.txt")]
c11 = [x for x in file if x % 11 == 0]
c17 = [x for x in file if x % 17 == 0]
if len(c11) > len(c17):
    print(len(c11), min(c11))
else:
    print(len(c17), max(c17))