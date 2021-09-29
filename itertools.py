from itertools import groupby
print(*[(int(k),len(list(c))) for k,c in groupby(input())])