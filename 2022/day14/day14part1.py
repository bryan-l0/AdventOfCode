def sim_sand(x, y):
    if max_y <= y:
        return False
    elif (x, y + 1) not in map:
        return sim_sand(x, y + 1)
    elif (x - 1, y + 1) not in map:
        return sim_sand(x - 1, y)
    elif (x + 1, y + 1) not in map:
        return sim_sand(x + 1, y)
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

def x(point):
    return point[0]
def y(point):
    return point[1]

with open('./day14/day14input.txt', 'r') as f:
    lines = [ l.strip() for l in f ] 

map = set()

for line in lines:
    points = line.split(' -> ')
    points = list(zip(points, points[1::]))
    for point in points:
        map = map.union(generate_map(point[0].split(','), point[1].split(',')))

print(len(map))

min_x = min(map, key=x)[0]
min_y = min(map, key=y)[1]
max_x = max(map, key=x)[0]
max_y = max(map, key=y)[1]

sand_count = 0
while True:
    sand = sim_sand(500, 0)
    if sand == False: break
    sand_count += 1
    map.add(sand)
print(len(map))
print(sand_count)