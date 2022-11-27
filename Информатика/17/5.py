a = [i for i in ([int(x) for x in open("17.txt")]) if hex(i)[-1]=="b" and i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0]
print(sum(a), len(a))