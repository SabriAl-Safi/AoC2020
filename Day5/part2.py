def seatID(s):
    return getCol(s) + (8 * getRow((s)))
                        
def getRow(s):
    return int(s[0:7].replace('B', '1').replace('F', '0'), 2)

def getCol(s):
    return int(s[7:10].replace('R', '1').replace('L', '0'), 2)

seatIDs = set([seatID(_) for _ in open('input.txt', 'r').readlines()])
rg = range(min(seatIDs), max(seatIDs))
print(next(i for i in rg if i not in seatIDs))
