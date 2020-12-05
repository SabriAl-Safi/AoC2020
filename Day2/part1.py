def isValid(s):
    sp = s.split(':')
    rule = parseRule(sp[0])
    pwd = sp[1]
    c = pwd.count(rule[2])
    return c >= rule[0] and c <= rule[1]

def parseRule(s):
    sp = s.split()
    rg = sp[0].split('-')
    return int(rg[0]), int(rg[1]), sp[1]

print(sum([isValid(_) for _ in open('input.txt', 'r').readlines()]))
