def total(range):
    return range[1] - range[0]

with open('./day15/day15input.txt', 'r') as f:
    lines = [ l.strip().split() for l in f ]

goal_y = 2_000_000
ranges = []
for line in lines:
    sensor_x = int(line[2][2:-1:])
    sensor_y = int(line[3][2:-1:])
    beacon_x = int(line[-2][2:-1:])
    beacon_y = int(line[-1][2::])
    manhattan = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    
    if manhattan < abs(goal_y - sensor_y):
        continue
    horizontal = manhattan - abs(goal_y - sensor_y)
    
    start_x = sensor_x - horizontal
    end_x = sensor_x + horizontal
    ranges.append((start_x, end_x))
ranges.sort()
print(ranges)
print(total(ranges[0]) + total((31358, 4424172)))