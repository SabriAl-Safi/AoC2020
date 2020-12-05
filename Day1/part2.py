nums = [int(x) for x in open('input.txt', 'r').readlines()]
numset= set(nums)
sumset = set([x+y for x in nums for y in nums])
a = next(n for n in nums if (2020-n) in sumset)
b = next(n for n in nums if ((2020-a)-n) in numset)
c = 2020 - (a+b)
print(a, b, c, a*b*c)
