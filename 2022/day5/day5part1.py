with open('day5input.txt', 'r') as f:
    l = f.readline()
    stack = [[], [], [], [], [], [], [], [], [], []]
    while True:
        if l[1] == '1': f.readline(); break
        for i in range(0, 9):
            if l[i * 4 + 1] != ' ':
                stack[i + 1].append(l[i * 4 + 1])
        l = f.readline()
    stack = [ i[::-1] for i in stack ]
    for l in f:
        t = l.strip().split(' ')
        quantity, start, end = int(t[1]), int(t[3]), int(t[5])
        for i in range(quantity): 
            stack[end].append(stack[start].pop())
    for i in stack[1::]: 
        print(i[-1], end='')
    print()