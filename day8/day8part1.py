with open('./day8/day8input.txt', 'r') as f:
    l = [l.strip() for l in f]

l2r, r2l, t2b, b2t, output = [], [], [], [], []
for i in l: 
    l2r.append([True] * len(l[0]))
    r2l.append([True] * len(l[0]))
    t2b.append([True] * len(l[0]))
    b2t.append([True] * len(l[0]))
    output.append([False] * len(l[0]))

current_maximum = 0
row_maximum = 0

for y in range(len(l)):
    current_maximum = l[y][0]
    row_maximum = max(l[y])
    end_of_line = False
    for x in range(1, len(l[0])):
        if end_of_line:
            l2r[y][x] = False
            continue
        if current_maximum < l[y][x]:
            current_maximum = l[y][x]
        else:
            l2r[y][x] = False
        if row_maximum == current_maximum:
            end_of_line = True

for y in range(len(l)):
    current_maximum = l[y][len(l) - 1]
    row_maximum = max(l[y])
    end_of_line = False
    for x in range(len(l[0])-2, -1, -1):
        if end_of_line:
            r2l[y][x] = False
            continue
        if current_maximum < l[y][x]:
            current_maximum = l[y][x]
        else:
            r2l[y][x] = False
        if row_maximum == current_maximum:
            end_of_line = True

for x in range(len(l[0])):
    current_maximum = l[0][x]
    row_maximum = max([row[x] for row in l])
    end_of_line = False
    for y in range(1, len(l)):
        if end_of_line:
            t2b[y][x] = False
            continue
        if current_maximum < l[y][x]:
            current_maximum = l[y][x]
        else:
            t2b[y][x] = False
        if row_maximum == current_maximum:
            end_of_line = True

for x in range(len(l[0])):
    current_maximum = l[len(l)-1][x]
    row_maximum = max([row[x] for row in l])
    end_of_line = False
    for y in range(len(l) - 2, -1, -1):
        if end_of_line:
            b2t[y][x] = False
            continue
        if current_maximum < l[y][x]:
            current_maximum = l[y][x]
        else:
            b2t[y][x] = False
        if row_maximum == current_maximum:
            end_of_line = True
count = 0
for y in range(len(l)):
    for x in range(len(l[0])):
        if l2r[y][x] or r2l[y][x] or t2b[y][x] or b2t[y][x]:
            count += 1
            output[y][x] = True
print(output)
print(count)

# output = []
# rows = [[True] * len(l[0])]
# cols = []
# for i in l: cols.append([True] * len(l[0]))
# for i in l: output.append([False] * len(l[0]))
# count = 0

# for y in range(1, len(l) - 1):
#     row = [True] * len(l[0])
#     left_current = l[y][0]
#     right_current = l[y][len(l[0]) - 1]
#     for x in range(1, len(l[0]) - 1):
#         print(l[y][x], l[y][x-1], left_current)
#         if l[y][x] < max(l[y][x-1], left_current):
#             row[x] = False
#         else:
#             left_current = l[y][x]
#         if left_current == 9: 
#             left_most = x + 1
#             break
#     for x in range(len(l[0]) - 2, 1, -1):
#         if l[y][x] < max(l[y][x+1], right_current):
#             row[x] = False
#         else:
#             right_current = l[y][x]
#         if right_current == 9:
#             right_most = x - 1
#             break
#     print(y, left_most, right_most)
#     print(row)
#     rows.append(row)

# rows.append([True] * len(l[0]))

# for x in range(1, len(l[0]) - 1):
#     top_most = 1
#     bottom_most = len(l) - 2
#     for y in range(1, len(l) - 1):
#         if not l[y - 1][x] <  l[y][x]:
#             top_most = y
#             break
#     for y in range(len(l) - 2, 1, -1):
#         if not l[y + 1][x] < l[y][x]:
#             bottom_most = y
#             break
#     for x in range(len(l[0])):
#         for y in range(top_most, bottom_most + 1):
#             cols[y][x] = False

# for y in range(len(l)):
#     for x in range(len(l[0])):
#         if rows[y][x] or cols[y][x]: count += 1
#         output[y][x] = rows[y][x] or cols[y][x]
# print(count)