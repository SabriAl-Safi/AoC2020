import math

def getNext(st, ts):
    return ((math.ceil(st/ts)) * ts) - st

i = open('input.txt', 'r').readlines()
start = int(i[0])
ids = [ int(_) for _ in i[1].split(',') if _ != 'x' ]
times = [ getNext(start, j) for j in ids]
minT = min(times)
minInd = times.index(minT)    
print(ids[minInd]*minT)
