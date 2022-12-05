max1, max2, max3, count = 0, 0, 0, 0
with open('day1input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line != '':
            count += int(line)
            continue
        if count >= max1: max1, max2, max3 = count, max1, max2
        elif count >= max2: max2, max3 = count, max2
        else: max3 = max(max3, count)
        count = 0
print(max1 + max2 + max3)