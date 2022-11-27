file = [int(x) for x in open("17_5.txt")]
a = [file[i] * file[i + 1] for i in range(len(file) - 1) if
     100 <= (file[i] + file[i + 1]) and ((file[i] < 0) or (file[i + 1] < 0))]
print(len(a), max(a))
