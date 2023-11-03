class Counter(dict):
    def __missing__(self, key):
        return 0

def cmp(head, tail):
    if tail < head:
        return 1
    elif head < tail:
        return -1
    else:
        return 0

def move_head(dir, start):
    if dir == 'R':
        return (start[0] + 1, start[1])
    if dir == 'L':
        return (start[0] - 1, start[1])
    if dir == 'U':
        return (start[0], start[1] + 1)
    if dir == 'D':
        return (start[0], start[1] - 1)

def move_tail(head, tail):
    x_diff, y_diff = tail[0] - head[0], tail[1] - head[1]
    x_diff, y_diff = abs(x_diff), abs(y_diff)
    direction_to_move = (cmp(head[0], tail[0]), cmp(head[1], tail[1]))
    if x_diff == 2 or y_diff == 2:
        return (tail[0] + direction_to_move[0], tail[1] + direction_to_move[1])
    return tail

def part1(input):
    dict = Counter()
    head = (0, 0)
    tail = (0, 0)
    for movement in input:
        for i in range(int(movement[1])):
            head = move_head(movement[0], head)
            tail = move_tail(head, tail)
            dict[tail] = dict[tail] + 1
    return(len(dict))

def part2(input):
    dict = Counter()
    knots = [(0, 0)] * 10
    for movement in input:
        for i in range(int(movement[1])):
            knots[0] = move_head(movement[0], knots[0])
            for j in range(1, 9):
                knots[j] = move_tail(knots[j - 1], knots[j])
            knots[9] = move_tail(knots[8], knots[9])
            dict[knots[9]] = dict[knots[9]] + 1
    return(len(dict))

with open('./day9/day9input.txt', 'r') as f:
    input = [ l.strip().split() for l in f ]

print(part1(input))
print(part2(input))