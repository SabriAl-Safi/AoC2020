def wd(arr):
    return range(len(arr))

def step(lo, adj):
    nlo = [ [ stepSeat(lo, i, j, adj) for j in wd(lo[i]) ] for i in wd(lo)]
    return nlo

def stepSeat(lo, i, j, adj):
    cur = lo[i][j]
    return '#' if cur == 'L' and numOcc(lo, adj[i][j]) == 0 \
        else 'L' if cur == '#' and numOcc(lo, adj[i][j]) >= 5 \
        else cur

def numOcc(lo, adj):
    return sum([ 1 for a in adj if lo[a[0]][a[1]]=='#' ])

def isEqual(a, b):
    return all([a[i][j] == b[i][j] for j in wd(a[0]) for i in wd(a)])

def getAdj(lo):
    return [ [ getAdjSeat(lo, i, j) for j in wd(lo[0]) ] for i in wd(lo) ]

def getAdjSeat(lo, i, j):
    angles = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    adjSeat = [getAdjSeatAngle(lo, i, j, a) for a in angles]
    return [_ for _ in adjSeat if _ is not None]

def getAdjSeatAngle(lo, i, j, a):
    ia = i + a[0]
    ja = j + a[1]
    while 0<=ia<len(lo) and 0<=ja<len(lo[0]) and lo[ia][ja]=='.':
        ia += a[0]
        ja += a[1]
    if 0<=ia<len(lo) and 0<=ja<len(lo[0]):
        return [ia, ja]

layout = [_.strip() for _ in open('input.txt', 'r').readlines()]
adj = getAdj(layout)
new = step(layout, adj)
while not isEqual(new, layout):
    layout, new = new, step(new, adj)
print(sum([1 for j in wd(new[0]) for i in wd(new) if new[i][j]=='#']))

