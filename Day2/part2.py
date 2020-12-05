def isValid(s):
    sp = s.split(':')
    rule = parseRule(sp[0])
    pwd = sp[1]
    c = set([pwd[rule[0]],pwd[rule[1]]])
    return rule[2] in c and len(c)==2

def parseRule(s):
    sp = s.split()
    rg = sp[0].split('-')
    return int(rg[0]), int(rg[1]), sp[1]

print(sum([isValid(_) for _ in open('input.txt', 'r').readlines()]))
