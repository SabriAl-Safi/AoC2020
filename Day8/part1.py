seen = set()
row = 0
acc = 0
boot = [i for i in open('input.txt', 'r').readlines()]

while row not in seen:
    seen.add(row)
    sp = boot[row].split()
    ins = sp[0]
    num = int(sp[1])
    if ins == 'jmp':
        row += num
    elif ins == 'acc':
        acc += num
        row += 1
    else:
        row += 1

print(acc)
