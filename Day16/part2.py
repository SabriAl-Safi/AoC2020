import math

def parseRules(rules):
    return { _.split(':')[0] : parse2Lims(_.split(':')[1]) for _ in rules.split('\n') }

def parse2Lims(s):
    return [ parseLims(i) for i in s.split(' or ') ]

def parseLims(s):
    return [ int(i) for i in s.split('-')]

def parseTicket(s):
    return [ int(i) for i in s.split(',') ]

def isTicketValid(t, r):
    return all( any(isValid(num, l) for l in r.values() ) for num in t  )

def isValid(n, r):
    return any( l[0] <= n <= l[1] for l in r )

def validPositions(rule, tickets):
    return set([ n for n in range(len(tickets[0])) if isPositionValid(rule, tickets, n)])

def isPositionValid(rule, tickets, p):
    return all([
        isValid(t[p], rule)
        for t in tickets ])

data = open('input.txt', 'r').read().split('\n\n')
rules = parseRules(data[0])
ticket = parseTicket(data[1].split('\n')[1])
nearby =  [ parseTicket(_) for _ in data[2].split('\n')[1:] ]
validTickets = [ n for n in nearby if isTicketValid(n, rules) ]
possibilities = { r : validPositions(rules[r], validTickets) for r in rules }

while any(len(possibilities[v]) > 1 for v in possibilities):
    known = set().union(*[_ for _ in possibilities.values() if len(_) == 1 ])
    possibilities = { r : possibilities[r]-known if len(possibilities[r]) > 1 else possibilities[r] for r in possibilities  }

positions = [ list(possibilities[r])[0] for r in rules if r[0:9] == 'departure' ]
values = [ ticket[p] for p in positions ]

print( math.prod(values))
