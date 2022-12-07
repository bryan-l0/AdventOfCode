with open('./day6/day6input.txt', 'r') as f:
    l = f.readline().strip()
    for i in range(14, len(l)):
        if len(set(l[i - 14:i])) == 14: print(i); break
