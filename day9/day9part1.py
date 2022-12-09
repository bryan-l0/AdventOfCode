class Counter(dict):
    def __missing__(self, key):
        return 0

def cmp(head, tail):
    if head > tail:
        return 1
    elif tail > head:
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
    x_diffm, y_diffm = abs(x_diff), abs(y_diff)
    direction_to_move = (cmp(head[0], tail[0]), cmp(head[1], tail[1]))
    if x_diffm == 2 or y_diffm == 2:
        return (tail[0] + direction_to_move[0], tail[1] + direction_to_move[1])
    return tail

with open('./day9/day9input.txt', 'r') as f:
    input = [ l.strip().split() for l in f ]

head_position = (0, 0)
tail_position = (0, 0)
dict = Counter()
for movement in input:
    for i in range(int(movement[1])):
        head_position = move_head(movement[0], head_position)
        tail_position = move_tail(head_position, tail_position)
        dict[tail_position] = dict[tail_position] + 1
print(len(dict))