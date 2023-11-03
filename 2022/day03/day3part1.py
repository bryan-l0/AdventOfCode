output = 0
with open('day3input.txt', 'r') as f:
    for l in f:
        l = l.strip()
        l1, l2 = set(l[:len(l)//2]), set(l[len(l)//2:])
        for i in l1:
            if i in l2: 
                if i.islower(): output += ord(i) - 96
                else: output += ord(i) - 38
                continue
print(output)