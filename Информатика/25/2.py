from fnmatch import *

for i in range(12347, 10 ** 8):
    if fnmatch(str(i), "1234*7") and i % 141 == 0:
        print(i, i // 141)
