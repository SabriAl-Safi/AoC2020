def wd(arr):
    return range(len(arr))

def step(lo):
    nlo = [ [ stepSeat(lo, i, j) for j in wd(lo[i]) ] for i in wd(lo)]
    return nlo

def stepSeat(lo, i, j):
    cur = lo[i][j]
    return '#' if cur == 'L' and numOcc(lo, i, j) == 0 \
        else 'L' if cur == '#' and numOcc(lo, i, j) >= 4 \
        else cur

def numOcc(lo, i, j):
    imin, imax = max(i-1, 0),min(i+1, len(lo)-1)
    jmin, jmax = max(j-1, 0), min(j+1, len(lo[0])-1)
    return sum([
        1
        for ja in range(jmin, jmax+1)
        for ia in range(imin, imax+1)
        if (not (ia==i and ja==j)) and (lo[ia][ja]=='#')])

def isEqual(a, b):
    return all([a[i][j] == b[i][j] for j in wd(a[0]) for i in wd(a)])

layout = [_.strip() for _ in open('input.txt', 'r').readlines()]
new = step(layout)
while not isEqual(new, layout):
    layout, new = new, step(new)
print(sum([1 for j in wd(new[0]) for i in wd(new) if new[i][j]=='#']))
