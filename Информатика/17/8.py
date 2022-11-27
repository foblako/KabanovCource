file = [int(x) for x in open("17_1.txt")]
a = [file[i] + file[i + 1] + file[i + 2] for i in range(len(file) - 2) if
     (file[i] * file[i + 1] * file[i + 2]) % 7 == 0 and (file[i] + file[i + 1] + file[i + 2]) % 10 == 5]
print(len(a), max(a))
