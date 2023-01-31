import numpy as np

with open('./day17/day17input.txt', 'r') as f:
    l = f.readline().strip()

input_length = len(l)

# Use Cartesian System

def rock0(): 
    return [(2, h + 3), (3, h + 3), (4, h + 3), (5, h + 3)]
def rock1():
    return [(3, h + 5), (2, h + 4), (3, h + 4), (4, h + 4), (3, h + 3)]
def rock2():
    return [(4, h + 5), (4, h + 4), (4, h + 3), (3, h + 3), (2, h + 3)]
def rock3():
    return [(2, h + 6), (2, h + 5), (2, h + 4), (2, h + 3)]
def rock4():
    return [(3, h + 4), (2, h + 4), (3, h + 3), (2, h + 3)]

def blow(_r):
    global index
    direction = l[index]
    index = (index + 1) % input_length
    if direction == '<' and len([ x for (x, _) in _r if x < 1]) == 0 and len(_r) == len([ x for (x, y) in _r if (x - 1, y) not in points ]):
        return [ (x - 1, y) for (x, y) in _r ]
    elif direction == '>' and len([ x for (x, _) in _r if x > 5]) == 0 and len(_r) == len([ x for (x, y) in _r if (x + 1, y) not in points ]):
        return [ (x + 1, y) for (x, y) in _r ]
    else:
        return _r


def drop(_r):
    global points
    if len(_r) == len([ x for (x, y) in _r if (x, y - 1) not in points ]):
        return [ (x, y - 1) for (x, y) in _r ]
    points += _r
    return False

def move(_r):
    global h
    _r = blow(_r)
    _r = drop(_r)
    if _r == False:
        h = max([y for (_, y) in points]) + 1
        return
    move(_r)

def pretty_print():
    global points
    max_y = max([ y for (_, y) in points ])
    arr = np.empty([max_y + 1, 7], int)
    for (x, y) in points:
        if y < 0:
            continue
        arr[y][x] = 7
    arr = np.flipud(arr)
    print(arr)
    print()


points = [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)]

h = 0
rock = 0
index = 0
while rock < 5050:
    r = eval(f'rock{rock % 5}()')
    move(r)
    # pretty_print()
    rock += 1
print(max([y for (_, y) in points]) + 1)
