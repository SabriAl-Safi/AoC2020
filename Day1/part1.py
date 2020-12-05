nums = [int(x) for x in open('input.txt', 'r').readlines()]
numset = set(nums)
l = next(n for n in nums if (2020-n) in numset)
print(l*(2020-l))
