from fnmatch import *

for x in range(700000, 100000000):
    if not fnmatch(str(x), "*0??3*") and not fnmatch(str(x), "*4??2*") and not fnmatch(str(x), "*1*") and x % 13 == 0:
        print(x, sum([int(i) for i in list(str(x))]))
