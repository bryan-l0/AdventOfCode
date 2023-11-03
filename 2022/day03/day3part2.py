output, l1, l2, l3 = 0, '', '', ''
with open('day3input.txt', 'r') as f:
    for l in f:
        if l1 == '': l1 = l.strip(); continue
        if l2 == '': l2 = l.strip(); continue
        if l3 == '': l3 = l.strip()
        for i in set(l1):
            if i in set(l2).intersection(l3):
                if i.islower(): output += ord(i) - 96
                else: output += ord(i) - 38
                l1, l2, l3 = '', '', ''
                break
print(output)