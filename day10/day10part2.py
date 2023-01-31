with open('./day10/day10input.txt') as f:
    lines = [ l.strip().split() for l in f ]

x = 1
cycle = 0
crt = 0

for line in lines:
    
    if line[0] == 'noop': 
        if crt in [x-1, x, x+1]: 
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        crt += 1
    if line[0] == 'addx':
        if crt in [x-1, x, x+1]: 
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        crt += 1
        if cycle % 40 == 0:
            print()
            crt = 0
        if crt in [x-1, x, x+1]: 
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        crt += 1
        x += int(line[1])
    if cycle % 40 == 0:
        print()
        crt = 0
        