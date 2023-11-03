with open('./day8/day8input.txt', 'r') as f:
    l = [l.strip() for l in f]

output = []
for i in l: 
    output.append([0] * len(l[0]))

for y in range(len(l)):
    for x in range(len(l[0])):
        left, right, up, down = 0, 0, 0, 0

        current_max = int(l[y][x])
        while True:
            # print(f'x: {x}, y: {y},', end=' ')
            if x - left - 1 < 0:
                break
            # print(l[y][x - left - 1], current_max)
            pointer = int(l[y][x - left - 1])
            left += 1
            if pointer < current_max:
                continue
            break

        current_max = int(l[y][x])
        while True:
            # print(f'x: {x}, y: {y},', end=' ')
            if x + right + 1 > len(l[0]) - 1:
                break
            # print(l[y][x - left - 1], current_max)
            pointer = int(l[y][x + right + 1])
            right += 1
            if pointer < current_max:
                continue
            break

        current_max = int(l[y][x])
        while True:
            # print(f'x: {x}, y: {y},', end=' ')
            if y - up - 1 < 0:
                break
            # print(l[y][x - left - 1], current_max)
            pointer = int(l[y - up - 1][x])
            up += 1
            if pointer < current_max:
                continue         
            break

        current_max = int(l[y][x])
        while True:
            # print(f'x: {x}, y: {y},', end=' ')
            if y + down + 1 > len(l) - 1:
                break
            # print(l[y][x - left - 1], current_max)
            pointer = int(l[y + down + 1][x])
            down += 1
            if pointer < current_max:
                continue
            break
        if left * right * up * down > 100:
            print(x, y)
        output[y][x] = left * right * up * down
print(output[3])
print(max([max(row) for row in output]))