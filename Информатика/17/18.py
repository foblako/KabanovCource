file = [int(x) for x in open("17_9.txt")]
a = [max(file[i], file[i + 1]) for i in range(len(file) - 1) if
     (file[i] % 9 == 0 and file[i + 1] % 8 == 3 and file[i + 1] % 9 != 0) or (
             file[i + 1] % 9 == 0 and file[i] % 8 == 3 and file[i] % 9 != 0)]
print(len(a), max(a))
