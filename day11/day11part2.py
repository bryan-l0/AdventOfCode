# monkeys = {}
# details = {}
# details = []
# with open('./day11/day11test.txt', 'r') as f:
#     for l in f:
#         l = l.strip()
#         if l == '':
#             monkeys.append(details); details = []
#         else:
#             details.append(l)
monkeys = {
                0: {'items': [76, 88, 96, 97, 58, 61, 67],      True: 2, False: 3, 'inspects': 0},
                1: {'items': [93, 71, 79, 83, 69, 70, 94, 98],  True: 5, False: 6, 'inspects': 0},
                2: {'items': [50, 74, 67, 92, 61, 76],                  True: 3, False: 1, 'inspects': 0},
                3: {'items': [76, 92],              True: 1, False: 6, 'inspects': 0},
                4: {'items': [74, 94, 55, 87, 62],                      True: 2, False: 0, 'inspects': 0},
                5: {'items': [59, 62, 53, 62],                              True: 4, False: 7, 'inspects': 0},
                6: {'items': [62],  True: 5, False: 7, 'inspects': 0},
                7: {'items': [85, 54, 53],                          True: 4, False: 0, 'inspects': 0}
          }
#         if l == '': 
#             monkeys[monkey] = details; details = {}
#             continue
#         if l.split()[0] == "Monkey": 
#             monkey = f'monkey{l.split()[1][:-1:]}'
#             continue
#         if l.split()[0] == "Starting": 
#             details['items'] =[ int(i.strip()) for i in l.split(':')[1].strip().split(',') ]
#             continue
#         if l.split()[0] == "Operation:":
#             details['operation'] = l.split()[-2::]
#             continue
#         if l.split()[0] == "Test:":
#             details['test'] = [l.split()[1], int(l.split()[3])]

# def worry(input, monkey):
#     if monkey == 0: return input * 19
#     if monkey == 1: return input + 6
#     if monkey == 2: return input * input
#     if monkey == 3: return input + 3
# def test(input, monkey):
#     if monkey == 0: return input % 23 == 0
#     if monkey == 1: return input % 19 == 0
#     if monkey == 2: return input % 13 == 0
#     if monkey == 3: return input % 17 == 0
def worry(input, monkey):
    if monkey == 0: return input * 19
    if monkey == 1: return input + 8
    if monkey == 2: return input * 13
    if monkey == 3: return input + 6
    if monkey == 4: return input + 5
    if monkey == 5: return input * input
    if monkey == 6: return input + 2
    if monkey == 7: return input + 3
def test(input, monkey):
    if monkey == 0: return input % 3 == 0
    if monkey == 1: return input % 11 == 0
    if monkey == 2: return input % 19 == 0
    if monkey == 3: return input % 5 == 0
    if monkey == 4: return input % 2 == 0
    if monkey == 5: return input % 7 == 0
    if monkey == 6: return input % 17 == 0
    if monkey == 7: return input % 13 == 0
def throw(input, monkey):
    monkeys[monkey]['items'].append(input)

for i in range(20):
    print(f'{i}/10000', end='\r')
    for monkey in monkeys:
        for _ in range(len(monkeys[monkey]['items'])):
            item = monkeys[monkey]['items'].pop(0)
            monkeys[monkey]['inspects'] += 1
            newitem = worry(item, monkey) // 3
            recipient = monkeys[monkey][test(newitem, monkey)]
            throw(newitem, recipient)
    print(monkeys)

output = [i['inspects'] for i in monkeys.values()]
output.sort()
print(output)
print(output[-1] * output[-2])