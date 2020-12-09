def isValidNum(c, i, p):
    return isDistinctSum(c[i-p:i], c[i])

def isDistinctSum(n, t):
    return len(set(n) & set([t-i for i in n])) > 1

def getRangeFrom(c, t, i):
    return next((c[i:j]
                 for j in range(i+2, len(c))
                 if sum(c[i:j]) == t),
                [])

code = [int(_) for _ in open('input.txt', 'r').readlines()]
preSize = 25
target = next(code[i]
              for i in range(preSize, len(code))
              if not isValidNum(code, i, preSize))
rg = next(getRangeFrom(code, target, i)
          for i in range(len(code))
          if len(getRangeFrom(code, target, i)) > 0)
print(min(rg) + max(rg))
