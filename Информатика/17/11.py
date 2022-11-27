file = [int(x) for x in open("17_6.txt")]
a = [file[i] + file[i + 1] + file[i + 2] + file[i + 3] for i in range(len(file) - 3) if
     file[i] >= file[i + 1] >= file[i + 2] >= file[i + 3] and (file[i] - file[i + 3]) > 1000]

print(len(a), min(a))
