file = [int(x) for x in open("17_3.txt")]
a = [(file[i] + file[i + 1] + file[i + 2]) for i in range(len(file) - 2) if
     (file[i] > sum(file) / len(file) and file[i + 1] > sum(file) / len(file) and file[i + 2] > sum(file) / len(
         file)) or (file[i] > sum(file) / len(file) and file[i + 1] > sum(file) / len(file)) or (
             file[i] > sum(file) / len(file) and file[i + 2] > sum(file) / len(file)) or (
                 file[i + 1] > sum(file) / len(file) and file[i + 2] > sum(file) / len(file))]
print(len(a), max(a))
