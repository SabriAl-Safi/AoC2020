import math

def numCollisions(angle_x, angle_y, t):
    return sum([isCollide(angle_x*i, angle_y*i, t) for i in range(len(t)//angle_y)])

def isCollide(x, y, t):
    return t[y][x % len(t[0])] == '#'
    
trees = [_.rstrip() for _ in open('input.txt', 'r').readlines()]
angles = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(math.prod([numCollisions(a[0], a[1], trees) for a in angles]))
