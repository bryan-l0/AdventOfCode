with open('./day12/day12input.txt', 'r') as f:
    l = [l.strip() for l in f]
    maze = []
    for line in range(len(l)):
        row = []
        for char in range(len(l[0])):
            c = ord(l[line][char])
            row.append(c)
            if c == 83:
                start = (char, line)
                row[-1] = 122
            if c == 69:
                end = (char, line)
                row[-1] = 122
        maze.append(row)

def manhattan(point):
    return max(abs(end[0] - point[0]) + abs(end[1] - point[1]), (122 - maze[point[1]][point[0]]))
    
def adjacent(point):
    output = []
    x, y = point[0], point[1]
    if x - 1 >= 0:
        if maze[y][x - 1] <= maze[y][x] + 1: 
            output.append((x - 1, y))
    if x + 1 < len(maze[0]):
        if maze[point[1]][x + 1] <= maze[y][x] + 1: 
            output.append((x + 1, y))
    if y - 1 >= 0:
        if maze[y - 1][point[0]] <= maze[y][x] + 1: 
            output.append((x, y - 1))
    if y + 1 < len(maze):
        if maze[y + 1][point[0]] <= maze[y][x] + 1: 
            output.append((x, y + 1))
    return output

def astar(e):
    return e[1]

point = (start, 0, 0)
stack = []
visited = set()
n = 0
while point[0] != end:
    visited.add(point[0])
    potentialpoints = adjacent(point[0])
    potentialpoints = [(p, point[1] + manhattan(p), point[2] + 1) for p in potentialpoints]
    stack += potentialpoints
    stack = [point for point in stack if point[0] not in visited]
    stack.sort(key=astar)
    point = stack.pop(0)
    n += 1
print(point)
print(len(visited))