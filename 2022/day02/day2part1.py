output = 0
points = { 'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2 }
with open('day2input.txt', 'r') as f:
    for l in f:
        l = l.strip().split(" ")
        output += points[l[1]] + 1
        if points[l[0]] == points[l[1]]: output += 3
        elif (points[l[0]] + 1) % 3 == points[l[1]]: output += 6
print(output)