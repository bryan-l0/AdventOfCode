def sim_sand1(x, y):
    if max_y <= y:
        return False
    elif (x, y + 1) not in map:
        return sim_sand1(x, y + 1)
    elif (x - 1, y + 1) not in map:
        return sim_sand1(x - 1, y)
    elif (x + 1, y + 1) not in map:
        return sim_sand1(x + 1, y)
    else:
        return x, y

def sim_sand2(x, y):
    if max_y + 1 == y:
        return x, y
    elif (x, y + 1) not in map:
        return sim_sand2(x, y + 1)
    elif (x - 1, y + 1) not in map:
        return sim_sand2(x - 1, y)
    elif (x + 1, y + 1) not in map:
        return sim_sand2(x + 1, y)
    else:
        return x, y

def generate_map(start, end):
    x0, y0 = start
    x1, y1 = end
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    output = set()
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            output.add((x0, y))
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            output.add((x, y0))
    return output

def get_new_map():
    map = set()
    for points in list_of_points:
        for point in points:
            map = map.union(generate_map(point[0].split(','), point[1].split(',')))
    return map

def y(point):
    return point[1]

def part1():
    sand_count = 0
    while True:
        sand = sim_sand1(500, 0)
        if sand == False: break
        sand_count += 1
        map.add(sand)
    return sand_count

def part2():
    sand_count = 0
    while True:
        sand = sim_sand2(500, 0)
        sand_count += 1
        if sand == (500 , 0): break
        map.add(sand)
    return sand_count

with open('./day14/day14input.txt', 'r') as f:
    lines = [ l.strip() for l in f ] 

map = set()

list_of_points = []
for line in lines:
    p = line.split(' -> ')
    p = list(zip(p, p[1::]))
    list_of_points.append(p)

map = get_new_map()
max_y = max(map, key=y)[1]

print(f'Part 1: {part1()}')
map = get_new_map()
print(f'Part 2: {part2()}')