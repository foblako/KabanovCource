a = [i for i in [int(x) for x in open("17.txt")] if i % 13 == 7 and i % 7 != 0 and i % 11 != 0]
print(max(a)-min(a), len(a))
