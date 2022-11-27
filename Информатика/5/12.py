print(max([n for n in range(1000, 10000) if
           int(str(min((int(str(n)[0]) * int(str(n)[1])), (int(str(n)[2]) * int(str(n)[3])))) + str(
               max((int(str(n)[0]) * int(str(n)[1])), (int(str(n)[2]) * int(str(n)[3]))))) == 1214]))
