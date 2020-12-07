from itertools import groupby

def parseRule(r):
    outer, inners = r.split('contain')
    if inners.strip() == "no other bags.":
        return []
    return [( innerClr(i), outerClr(outer) ) for i in inners.split(',')]

def innerClr(s):
    return ' '.join(s.split()[1:-1])

def outerClr(s):
    return ' '.join(s.split()[:-1])

def outermosts(bag, containers):
    if bag not in containers:
        return []
    cont = containers[bag]
    return cont + [x for o in cont for x in outermosts(o, containers) ]

rules = [r for _ in open('input.txt', 'r').readlines() for r in parseRule(_) ]
containers = { g[0] : [ h[1] for h in g[1] ] for g in groupby(sorted(rules), lambda x : x[0]) }
print(len(set(outermosts('shiny gold', containers))))
