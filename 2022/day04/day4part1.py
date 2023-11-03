with open('day4input.txt', 'r') as f:
    output = 0
    for l in f:
        l = l.strip().split(',')
        l0, l1 = l[0].split('-')[0], l[0].split('-')[1]
        r0, r1 = l[1].split('-')[0], l[1].split('-')[1]
        l0, l1, r0, r1 = int(l0), int(l1), int(r0), int(r1)
        if l0 <= r0 and l1 >= r1: output += 1; continue
        if r0 <= l0 and r1 >= l1: output += 1
print(output)