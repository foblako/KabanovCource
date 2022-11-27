file = [int(x) for x in open("17_11.txt")]
d35 = sum([int(k) for x in file if x % 35 == 0 for k in str(x)])
a = [file[i] + file[i + 1] for i in range(len(file) - 1) if
     (file[i] > d35 and file[i + 1] < d35 and hex(file[i + 1])[-1] == "f" and hex(file[i + 1])[-2] == "e") or (
             file[i + 1] > d35 and file[i] < d35 and hex(file[i])[-1] == "f" and hex(file[i])[-2] == "e")]
print(len(a), min(a))
