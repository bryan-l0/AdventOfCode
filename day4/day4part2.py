import re
with open('day4input.txt', 'r') as f:
    output = 0
    for l in f:
        l = re.split('-|,', l.strip())
        l0, l1, r0, r1 = int(l[0]), int(l[1]), int(l[2]), int(l[3])
        if l0 <= r1 and l1 >= r0: output += 1; continue
print(output)