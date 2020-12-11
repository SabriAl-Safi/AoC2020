rat = [0] + sorted([int(_) for _ in open('input.txt', 'r').readlines()])
ars = [0 for i in rat]
ars[0] = 1

for i in range(1, len(rat)):
    n = ars[i-1]
    if i > 1 and (rat[i] - rat[i-2] <= 3):
        n += ars[i-2]
    if i > 2 and (rat[i] - rat[i - 3] <= 3):
        n += ars[i - 3]
    ars[i] = n

print(ars[-1])
