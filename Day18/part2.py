def evaluate(s):
    if len(s) == 1:
        return s
    idx = pivot(s, '*')
    if (idx >= 0):
        return eval(str(evaluate(s[:idx])) + s[idx] + str(evaluate(s[idx+1:])))
    idx = pivot(s, '+')
    if (idx >= 0):
        return eval(str(evaluate(s[:idx])) + s[idx] + str(evaluate(s[idx+1:])))
    return evaluate(s[1:-1])

def pivot(s, o):
    lvl = 0
    for i, c in enumerate(s[::-1]):
        if c == ')':
            lvl+=1
        elif c == '(':
            lvl-=1
        elif (c==o) and lvl == 0:
            return len(s)-(i+1)
    return -1

print(sum([ evaluate(_.replace(' ','').strip()) for _ in open('input.txt', 'r').readlines()]))
