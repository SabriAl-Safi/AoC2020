dVec = { 'N': [1, 0], 'S': [-1, 0], 'E': [0, 1], 'W': [0, -1] }
d = [ 'N', 'E', 'S', 'W' ]

def sumArr(x, y):
    return [x[i] + y[i] for i in range(len(x))]

def mulArr(v, a):
    return [v * i for i in a]

def move(p, b, a, v):
    if a == 'F':
        return move(p, b, d[b], v)
    if a in dVec:
        mulVec = mulArr(v, dVec[a])
        return sumArr(p, mulVec), b
    rot = v//90 if a=='R' else -v//90
    return p, (b + rot)%4

ins = [[x[0], int(x[1:])] for x in open('input.txt', 'r').readlines()]
p = [0,0]
b = 1
for i in ins:
    p, b = move(p, b, i[0], i[1])
print(p, b)
print(abs(p[0]) + abs(p[1]))
