def getResult(bootCode):
    seen = set()
    row = 0
    acc = 0
    while row not in seen and row < len(bootCode):
        seen.add(row)
        sp = bootCode[row].split()
        ins = sp[0]
        num = int(sp[1])
        if ins == 'jmp':
            row += num
        elif ins == 'acc':
            acc += num
            row += 1
        else:
            row += 1

    if row == len(bootCode):
        return acc
    return None

def getAlts(bootCode):
    alts = [getAlt(bootCode, i) for i in range(len(bootCode))]
    return [bootCode] + [_ for _ in alts if _ is not None]

def getAlt(bootCode, i):
    rule = bootCode[i]
    sp = rule.split()
    ins = sp[0]
    if ins == 'acc':
        return None
    elif ins == 'jmp':
        newIns = 'nop'
    else:
        newIns = 'jmp'
    newRule = newIns + ' ' + sp[1]
    newBootCode = [_ for _ in bootCode]
    newBootCode[i] = newRule
    return newBootCode

bc = [i.strip() for i in open('input.txt', 'r').readlines()]

for alt in getAlts(bc):
    g = getResult(alt)
    if g is None:
        continue
    print(g)
    break
