import math

def bezout(a, b):
    si, si1 = 0, 1
    ti, ti1 = 1, 0
    ri = 1
    while ri != 0:
        q = a // b
        ri1, ri = ri, a % b
        a, b = b, ri
        si, si1 = si1 - q*si, si
        ti, ti1 = ti1 - q*ti, ti
    return si1, ti1, ri1

ids = [_ for _ in open('input.txt', 'r').readlines()[1].split(',')]
p = int(ids[0])
c = 0
pIdx = 0

for idx, nStr in enumerate(ids):
    if idx == 0 or nStr == 'x':
        continue

    n = int(nStr)
    s, t, r = bezout(n, p)
    d = c - pIdx + idx
    c = d + ((-t)*d*p)
    p = n*p
    c = c%p
    pIdx = idx

print(c-pIdx)
