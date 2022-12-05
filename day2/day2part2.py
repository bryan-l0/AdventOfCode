output = 0
points = { 'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 3, 'Z': 6 }
result = { 'X': -1, 'Y': 0, 'Z': 1}
with open('day2input.txt', 'r') as f:
    for l in f:
        l = l.strip().split(" ")
        output += (points[l[0]] + result[l[1]]) % 3 + points[l[1]] + 1
print(output)