with open('day5input.txt', 'r') as f:
    l = f.readline()
    stack = [[], [], [], [], [], [], [], [], [], []]
    while l[1] != '1':
        for i in range(0, 9):
            if l[i * 4 + 1] != ' ':
                stack[i + 1].append(l[i * 4 + 1])
        l = f.readline()
    f.readline()
    for i in stack:
        i.reverse()
    for l in f:
        t = l.strip().split(' ')
        quantity, start, end = int(t[1]), int(t[3]), int(t[5])
        stack[end] += stack[start][-quantity::]
        stack[start] = stack[start][:-quantity:]
    print(stack)
    for i in stack[1::]:
        print(i[-1],end='')