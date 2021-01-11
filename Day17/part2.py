def neighbours(c):
    return [ (c[0]+i-1,c[1]+j-1,c[2]+k-1,c[3]+l-1)
             for i in range(3)
             for j in range(3)
             for k in range(3)
             for l in range(3)
             if not (i==1 and j==1 and k==1 and l==1) ]

def iterate(active):
    sa = set(active)
    an = [ n for a in active for n in neighbours(a) ]
    da = { }
    for n in an:
        if n in da:
            da[n]+=1
        else:
            da[n]=1
    return [ a for a in da if da[a]==3 or (da[a]==2 and a in sa) ]
                

data = [ _.strip() for _ in open('input.txt', 'r').readlines()]

activeCells = [ (x, y, 0, 0)
                for x in range(len(data[0]))
                for y in range(len(data))
                if data[y][x] == '#' ]

for i in range(6):
    activeCells = iterate(activeCells)

print(len(activeCells))
