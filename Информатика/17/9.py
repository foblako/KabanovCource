file = [int(x) for x in open("17_1.txt")]
a = [(file[i] + file[i + 1] + file[i + 2]) // 3 for i in range(len(file) - 2) if
     (file[i] % 12 == 0 or file[i + 1] % 12 == 0 or file[i + 2] % 12 == 0) and (file[i] % 3 == 0 and file[i + 1] % 3 == 0 and file[i + 2] % 3 == 0)]
print(len(a), min(a))
