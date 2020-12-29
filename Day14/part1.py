mem = {}

def toBits(n):
    return bin(n)[2:].zfill(36)

def applyMask(bits, mask):
    return str.join('', [applyMaskBit(bits[i], mask[i]) for i in range(len(bits))])

def applyMaskBit(bit, mask):
    return bit if mask == 'X' else mask

for ins in open('input.txt', 'r').readlines():
    split = ins.split(' = ')

    if split[0] == 'mask':
        mask = split[1]
        continue

    reg = int(split[0][4:-1])
    val = toBits(int(split[1]))
    result = applyMask(val, mask)
    mem[reg] = int(result, 2)

print(sum(mem.values()))
