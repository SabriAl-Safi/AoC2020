from collections import defaultdict

def parseRules(s):
    x = [ _.split(':') for _ in s.split('\n')]
    x.sort(key=lambda z:int(z[0]))
    return [ parseRule(_[1].strip()) for _ in x]

def parseRule(s):
    if s[0] == '"':
        return set([s.replace('"','')])
    return [ list(map(int, _.strip().split(' '))) for _ in s.split('|') ]

def cat(x, k):
    if len(x) == 1:
        return list(k[x[0]])
    return [ y+z for y in list(k[x[0]]) for z in cat(x[1:],k) ]

def isValid(s, k):
    num42 = 0
    num31 = 0
    while len(s) >= 8 and s[:8] in k[42]:
        num42 += 1
        s = s[8:]
    while len(s) >= 8 and s[:8] in k[31]:
        num31 += 1
        s = s[8:]
    return s == '' and num31 > 0 and num42 > num31

data = open('input.txt').read().split('\n\n')
rules = parseRules(data[0])
msgs = data[1].split('\n')
known = defaultdict(set)
known[18] = set('a')
known[39] = set('b')
while 0 not in known:
    for i, r in enumerate(rules):
        if i in known:
            continue
        if any(_ not in known.keys() for x in r for _ in x):
            continue
        for x in r:
            for y in cat(x, known):
                known[i].add(y)

print(sum([ isValid(_, known) for _ in msgs ]))
