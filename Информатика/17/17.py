file = [int(x) for x in open("17_8.txt")]
sum4 = [x for x in file if x % 10 == 4]
sum4 = max(sum4)+min(sum4)
a = [file[i]+file[i+1] for i in range(len(file)-1) if (file[i]+file[i+1]) < sum4]
print(len(a), max(a))
