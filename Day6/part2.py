def yesCount(s):
    return len(set.intersection(*[set(_) for _ in s.split('\n')]))

print(sum([yesCount(_) for _ in open('input.txt', 'r').read().split('\n\n')]))
