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
print(sum([ _ in known[0] for _ in msgs ]))
