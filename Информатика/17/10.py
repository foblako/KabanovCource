def convert3(x):
    s = ""
    while x != 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


file = [int(x) for x in open("17_2.txt")]
a = [(file[i], file[i + 1], file[i + 2]) for i in range(len(file) - 2) if
     convert3(file[i])[-1] == "2" or convert3(file[i + 1])[-1] == "2" or convert3(file[i + 2])[-1] == "2"]
print(len(a), sum([min(i) for i in a]))
