with open('./day10/day10input.txt') as f:
    lines = [ l.strip().split() for l in f ]

total = 0
x = 1
cycle = 1
for line in lines:
    if line[0] == 'noop':
        if (cycle + 20) % 40 == 0:
            total += cycle * x
        cycle += 1
    if line[0] == 'addx':
        if (cycle + 20) % 40 == 0:
            total += cycle * x
        cycle += 1
        if (cycle + 20) % 40 == 0:
            total += cycle * x
        cycle += 1
        x += int(line[1])
        
print(total)