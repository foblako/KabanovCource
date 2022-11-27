file = [int(x) for x in open("17_1.txt")]
a = [file[i] * file[i + 1] for i in range(len(file)-1) if (file[i] * file[i + 1]) > 0 and (file[i] + file[i + 1]) % 7 == 0]
print(len(a), min(a))
