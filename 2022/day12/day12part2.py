start = []
with open('./day12/day12input.txt', 'r') as f:
    l = [l.strip() for l in f]
    maze = []
    for line in range(len(l)):
        row = []
        for char in range(len(l[0])):
            c = ord(l[line][char])
            row.append(c)
            if c == 97:
                start.append((char, line))
            if c == 69:
                end = (char, line)
                row[-1] = 122
        maze.append(row)

def manhattan(point):
    return abs(end[0] - point[0]) + abs(end[1] - point[1])
    
def adjacent(point):
    output = []
    x, y = point[0], point[1]
    if x - 1 >= 0:
        if 97 < maze[y][x - 1] <= maze[y][x] + 1: 
            output.append((x - 1, y))
    if x + 1 < len(maze[0]):
        if 97 < maze[point[1]][x + 1] <= maze[y][x] + 1: 
            output.append((x + 1, y))
    if y - 1 >= 0:
        if 97 < maze[y - 1][point[0]] <= maze[y][x] + 1: 
            output.append((x, y - 1))
    if y + 1 < len(maze):
        if 97 < maze[y + 1][point[0]] <= maze[y][x] + 1: 
            output.append((x, y + 1))
    return output

output = []
for p in start:
    point = (p, 0, 0)
    stack = []
    visited = set()
    b = False
    while point[0] != end:
        try:
            if point[2] > output[0][2]:
                break
        except:
            pass
        potentialpoints = adjacent(point[0])
        potentialpoints = [(p, point[1] + manhattan(p), point[2] + 1) for p in potentialpoints]
        stack += potentialpoints
        d = []
        if maze[point[0][1]][point[0][0]] == 97:
            new_a = point
        for i in range(len(stack)):
            if stack[i][0] in visited:
                d.append(i)
        visited.add(point[0])
        for i in d[::-1]:
            stack.pop(i)
        try:
            point = stack.pop(0)
        except:
            b = True
            break
    if b: continue
    output.append(point)
    t = [ t[2] for t in output ]
    output = [output[t.index(min(t))]]
print(output)