mem = {}

def toBits(n):
    return bin(n)[2:].zfill(36)

def applyMask(bits, mask):
    return str.join('', [applyMaskBit(bits[i], mask[i]) for i in range(len(bits))])

def applyMaskBit(bit, mask):
    return bit if mask == '0' else mask

def xIndices(bits):
    return [i for i,b in enumerate(bits) if b == 'X']

def floatResult(bits):
    ind = xIndices(bits)
    return [ floatResultBits(bits, i, ind) for i in range(2**len(ind)) ]

def floatResultBits(bits, i, ind):
    floatBits = bin(i)[2:].zfill(len(ind))
    newBits = [_ for _ in bits]
    for j in range(len(ind)):
        newBits[ind[j]] = floatBits[j]
    return str.join('', newBits)

for ins in open('input.txt', 'r').readlines():
    split = ins.split(' = ')

    if split[0] == 'mask':
        mask = split[1]
        continue

    reg = toBits(int(split[0][4:-1]))
    val = int(split[1])
    results = floatResult(applyMask(reg, mask))
    for r in results:
        mem[int(r,2)] = val

print(sum(mem.values()))
