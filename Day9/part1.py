def isValidNum(c, i, p):
    return isDistinctSum(c[i-p:i], c[i])

def isDistinctSum(n, t):
    return len(set(n) & set([t-i for i in n])) > 1

code = [int(_) for _ in open('input.txt', 'r').readlines()]
print(next(code[i] for i in range(25, len(code)) if not isValidNum(code, i, 25)))
