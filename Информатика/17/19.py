file = [int(x) for x in open("17_10.txt")]
a = [file[i] + file[i + 1] + file[i + 2] for i in range(len(file) - 2) if
     file[i + 1] % 10 == 9 and file[i + 1] > 0 and not (file[i] > 0 and file[i] % 10 == 9) and not (
                 file[i + 2] > 0 and file[
             i + 2] % 10 == 9)]
print(len(a), max(a))
