file = [int(x) for  x in open("17_4.txt")]
a = [(file[i], file[i+1]) for i in range(len(file)-1) if 50 <= (abs(file[i]) + abs(file[i+1])) <= 200]
print(len(a), min([i for i in a]))