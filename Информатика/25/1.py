from fnmatch import *

for x in range(123450608, 10 ** 9):
    if fnmatch(str(x), "12345?6?8") and x % 17 == 0:
        print(x, x / 17)
