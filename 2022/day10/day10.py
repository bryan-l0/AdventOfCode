with open('./day10/day10input.txt') as f:
    instructions = [l.strip().split() for l in f]

state = "Read Line"
x, cycle, part1, part2 = 1, 0, 0, ''
while len(instructions) > 0 or state != "Read Line":
    # Reads new instruction if no instruction loaded
    if state == "Read Line":
        l = instructions.pop(0)
        if l[0] == 'noop':
            state = "Read Line"
        elif l[0] == 'addx':
            state = "First Add"

    # Main Logic for the Solution
    part2 += '#' if cycle % 40 in [x-1, x, x+1] else '.'
    cycle += 1
    part1 += cycle * x if (cycle + 20) % 40 == 0 else 0
    if cycle % 40 == 0: part2 += '\n'

    # Finishes the Cycle
    if state == "Second Add":
        x += int(l[1])
        state = "Read Line"
    if state == "First Add":
        state = "Second Add"

print(f'Part 1: {part1}\n{part2}')