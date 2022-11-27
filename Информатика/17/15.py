file = [int(x) for x in open("17_7.txt")]
maxd19 = max([x for x in file if x % 19 == 0])
a = [file[i] + file[i + 1] for i in range(len(file) - 1) if (file[i] > maxd19 or file[i + 1] > maxd19)]
print(len(a), min(a))