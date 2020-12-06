def yesCount(s):
    return len(set(s.replace('\n','')))

print(sum([yesCount(_) for _ in open('input.txt', 'r').read().split('\n\n')]))
