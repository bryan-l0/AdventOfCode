with open('./day6/day6input.txt', 'r') as f:
    l = f.readline().strip()
    for i in range(4, len(l)):
        if len(set(l[i - 4:i])) == 4: print(i); break
