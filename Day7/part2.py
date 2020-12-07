from itertools import groupby

def parseRule(r):
    outer, inners = r.split('contain')
    if inners.strip() == "no other bags.":
        return []
    return outerClr(outer), [(innerClr(i), innerNum(i) ) for i in inners.split(',')]

def innerNum(s):
    return s.split()[0]

def innerClr(s):
    return ' '.join(s.split()[1:-1])

def outerClr(s):
    return ' '.join(s.split()[:-1])

def numInside(bag, inners):
    if bag not in inners:
        return 1
    return 1 + sum([int(i[1]) * numInside(i[0], inners) for i in inners[bag]])

rules = [ parseRule(_) for _ in open('input.txt', 'r').readlines() ]
inners = { r[0]: r[1] for r in rules if len(r) == 2}
print(numInside('shiny gold', inners) - 1)
