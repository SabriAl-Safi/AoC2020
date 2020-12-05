def isCollide(x, y, t):
    return t[y][x % len(t[0])] == '#'
    
trees = [_.rstrip() for _ in open('input.txt', 'r').readlines()]
print(sum([isCollide(3*i, i, trees) for i in range(len(trees))]))
