from datetime import datetime
start = datetime.now()
with open('./day15/day15input.txt', 'r') as f:
    lines = [ l.strip().split() for l in f ]

ranges = []
possible_points = []
for line in lines:
    sensor_x = int(line[2][2:-1:])
    sensor_y = int(line[3][2:-1:])
    beacon_x = int(line[-2][2:-1:])
    beacon_y = int(line[-1][2::])
    manhattan = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    ranges.append(((sensor_x, sensor_y), manhattan))

for i in range(4_000_001):
    range = []
    for sensor in ranges:
        sensor_x, sensor_y = sensor[0]
        manhattan = sensor[1]
        if manhattan < abs(i - sensor_y):
            continue
        horizontal = manhattan - abs(i - sensor_y)
        start_x, end_x = sensor_x - horizontal, sensor_x + horizontal
        range.append((start_x, end_x))
    range.sort()
    j = 0
    while len(range) > 1 and j + 1 < len(range):
        if range[j + 1][0] <= range[j][1] + 1:
            point = (min(range[j][0], range[j + 1][0]), max(range[j][1], range[j + 1][1]))
            range.pop(j + 1)
            range[j] = point
        else:
            j += 1
    if len(range) > 1:
        print(i, range)
        break
print(f'Time taken: {datetime.now() - start}s')