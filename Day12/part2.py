dVec = { 'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0] }

def sumArr(x, y):
    return [x[i] + y[i] for i in range(len(x))]

def mulArr(v, a):
    return [v * i for i in a]

def subArr(x, y):
    return [x[i] - y[i] for i in range(len(x))]

def rotR(a):
    return [ a[1], -a[0] ]

def move(ps, pw, a, v):
    
    if a == 'F':
        return ( sumArr(ps, mulArr(v, pw)) ), pw
    
    if a in dVec:
        return ps, sumArr(pw, mulArr(v, dVec[a]))
    
    numRot = v//90 if a=='R' else -v//90
    for i in range(numRot%4):
        pw = rotR(pw)
    
    return ps, pw

ins = [[x[0], int(x[1:])] for x in open('input.txt', 'r').readlines()]
ps = [0,0]
pw = [10,1]
for i in ins:
    ps, pw = move(ps, pw, i[0], i[1])  
print(ps, pw)
print(abs(ps[0]) + abs(ps[1]))
