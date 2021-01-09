def parseRules(rules):
    return { _.split(':')[0] : parse2Lims(_.split(':')[1]) for _ in rules.split('\n') }

def parse2Lims(s):
    return [ parseLims(i) for i in s.split(' or ') ]

def parseLims(s):
    return [ int(i) for i in s.split('-')]

def parseTicket(s):
    return [ int(i) for i in s.split(',') ]

def ticketErrorRate(t, r):
    return sum([
        num
        for num in t
        if not any([
            isValid(num, l)
            for l in r.values() ]) ])

def isValid(n, r):
    return any([ l[0] <= n <= l[1] for l in r ])

data = open('input.txt', 'r').read().split('\n\n')
rules = parseRules(data[0])
ticket = parseTicket(data[1].split('\n')[1])
nearby =  [ parseTicket(_) for _ in data[2].split('\n')[1:] ]
print(sum([ ticketErrorRate(n, rules) for n in nearby ]))
