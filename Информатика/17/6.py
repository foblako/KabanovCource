file = [int(x) for x in open("17_1.txt")]
a = [file[i] + file[i + 1] for i in range(len(file) - 1) if
     (file[i] + file[i + 1]) % 3 == 0 and (file[i] + file[i + 1]) % 6 != 0 and abs((file[i] * file[i + 1])) % 10 == 8]
print(len(a), max(a))
