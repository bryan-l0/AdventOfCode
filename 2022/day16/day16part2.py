import copy
from datetime import datetime 
import re
from itertools import product

start = datetime.now()
print(f'Started at {start}')

with open('./day16/day16input.txt', 'r') as f:
    lines = [ l.strip().split('=') for l in f ]
    tunnels = [ l[0].split()[1] for l in lines ]
    flow = [ int(l[1].split(';')[0]) for l in lines ]
    mapping = { k: v for (k, v) in zip(tunnels, flow) }

def tunnels_with_flow():
    return set([ k for k in mapping if mapping[k] != 0 ])

def mapping_drop_no_flow(map):
    return [ k for k in map if map[k] > 0 ]

def get_distance(start, end):
    return cache[start][end]
    # return cache[f'{start}{end}']

def get_total_flow(array, time):
    output = [ (time - array[key]) * mapping[key] for key in array ]
    return sum(output)

class Counter(dict):
    def __missing__(self, key):
        return []

# Cache all tunnel times
cache = {'XK': {'YH': 2, 'XS': 2, 'RA': 2, 'NM': 3, 'EA': 4, 'YP': 5, 'EI': 5, 'NU': 6, 'CX': 6, 'ZG': 6, 'WK': 7, 'QC': 7, 'NC': 8, 'MW': 8}, 'EI': {'RA': 3, 'MW': 3, 'XK': 5, 'EA': 5, 'XS': 6, 'YH': 7, 'NU': 7, 'CX': 7, 'ZG': 7, 'WK': 8, 'QC': 8, 'NM': 8, 'NC': 9, 'YP': 10}, 'CX': {'NU': 2, 'QC': 2, 'EA': 2, 'WK': 3, 'ZG': 4, 'RA': 4, 'NC': 5, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'EA': {'CX': 2, 'ZG': 2, 'RA': 2, 'NU': 4, 'QC': 4, 'NC': 4, 'XK': 4, 'EI': 5, 'XS': 5, 'WK': 5, 'YH': 6, 'NM': 7, 'MW': 8, 'YP': 9}, 'XS': {'XK': 2, 'RA': 3, 'YH': 4, 'EA': 5, 'NM': 5, 'EI': 6, 'NU': 7, 'CX': 7, 'ZG': 7, 'YP': 7, 'WK': 8, 'QC': 8, 'NC': 9, 'MW': 9}, 'NM': {'YH': 2, 'YP': 2, 'XK': 3, 'XS': 5, 'RA': 5, 'EA': 7, 'EI': 8, 'NU': 9, 'CX': 9, 'ZG': 9, 'WK': 10, 'QC': 10, 'NC': 11, 'MW': 11}, 'NC': {'ZG': 2, 'WK': 2, 'EA': 4, 'NU': 4, 'QC': 4, 'CX': 5, 'RA': 6, 'XK': 8, 'EI': 9, 'XS': 9, 'YH': 10, 'NM': 11, 'MW': 12, 'YP': 13}, 'MW': {'EI': 3, 'RA': 6, 'XK': 8, 'EA': 8, 'XS': 9, 'YH': 10, 'NU': 10, 'CX': 10, 'ZG': 10, 'WK': 11, 'QC': 11, 'NM': 11, 'NC': 12, 'YP': 13}, 'RA': {'XK': 2, 'EA': 2, 'EI': 3, 'XS': 3, 'YH': 4, 'NU': 4, 'CX': 4, 'ZG': 4, 'WK': 5, 'QC': 5, 'NM': 5, 'NC': 6, 'MW': 6, 'YP': 7}, 'NU': {'CX': 2, 'WK': 2, 'QC': 2, 'ZG': 3, 'EA': 4, 'NC': 4, 'RA': 4, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'YH': {'NM': 2, 'XK': 2, 'YP': 4, 'XS': 4, 'RA': 4, 'EA': 6, 'EI': 7, 'NU': 8, 'CX': 8, 'ZG': 8, 'WK': 9, 'QC': 9, 'NC': 10, 'MW': 10}, 'YP': {'NM': 2, 'YH': 4, 'XK': 5, 'XS': 7, 'RA': 7, 'EA': 9, 'EI': 10, 'NU': 11, 'CX': 11, 'ZG': 11, 'WK': 12, 'QC': 12, 'NC': 13, 'MW': 13}, 'ZG': {'NC': 2, 'EA': 2, 'NU': 3, 'WK': 4, 'CX': 4, 'RA': 4, 'QC': 5, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'QC': {'NU': 2, 'WK': 2, 'CX': 2, 'NC': 4, 'EA': 4, 'RA': 5, 'ZG': 5, 'XK': 7, 'EI': 8, 'XS': 8, 'YH': 9, 'NM': 10, 'MW': 11, 'YP': 12}, 'WK': {'NU': 2, 'NC': 2, 'QC': 2, 'CX': 3, 'ZG': 4, 'RA': 5, 'EA': 5, 'XK': 7, 'EI': 8, 'XS': 8, 'YH': 9, 'NM': 10, 'MW': 11, 'YP': 12}, 'AA': {'RA': 2, 'NU': 2, 'WK': 3, 'QC': 3, 'CX': 3, 'XK': 4, 'EA': 4, 'NC': 5, 'ZG': 5, 'EI': 5, 'XS': 5, 'YH': 6, 'NM': 7, 'MW': 8, 'YP': 9}}
# cache = {'BB': {'CC': 1, 'DD': 2, 'EE': 3, 'JJ': 3, 'HH': 6}, 'CC': {'BB': 1, 'DD': 1, 'EE': 2, 'JJ': 4, 'HH': 5}, 'DD': {'EE': 1, 'CC': 1, 'BB': 2, 'JJ': 3, 'HH': 4}, 'EE': {'DD': 1, 'CC': 2, 'BB': 3, 'HH': 3, 'JJ': 4}, 'HH': {'EE': 3, 'DD': 4, 'CC': 5, 'BB': 6, 'JJ': 7}, 'JJ': {'BB': 3, 'DD': 3, 'EE': 4, 'CC': 4, 'HH': 7}, 'AA': {'BB': 1, 'DD': 1, 'EE': 2, 'CC': 2, 'JJ': 2, 'HH': 5}}



# History, Mapping, Time, Open Time, Open Times Length
stack = [(['AA'], mapping_drop_no_flow(mapping), 1, {}, 0)]

maximum = -1
time = 27
flows = len(tunnels_with_flow())

best_20 = Counter()
while len(stack) > 0:
    current = stack.pop()
    key = current[0][-1]
    if current[2] > time:
        water = get_total_flow(current[3], time)
        if water < 1000:
            continue
        c = current[0]
        c.sort()
        c = ''.join(c)
        best_20[c] = best_20[c] + [water]
        continue
    if key in current[1]:
        current[3][key] = current[2] + 1
        current = (current[0], current[1], current[2] + 1, current[3], current[4])
        current[1].remove(key)
    if current[2] > time:
        water = get_total_flow(current[3], time)
        if water < 1000:
            continue
        c = current[0]
        c.sort()
        c = ''.join(c)
        best_20[c] = best_20[c] + [water]
        continue
    for k in current[1]:
        stack.append(((current[0] + [k]), copy.deepcopy(current[1]), current[2] + get_distance(key, k), copy.deepcopy(current[3]), current[4] + 1))
for key in best_20:
    best_20[key].sort(reverse=True)
    best_20[key] = best_20[key][0]
    
best_permutation = -1
l = sum(1 for _ in product(best_20, best_20))
print("Checking Combinations")
for i, (key1, key2) in enumerate(product(best_20, best_20)):
    if i % 100_000 == 0:
        print(f'\rLoop {i} out of {l}', end='') 
    k1 = re.compile('(..)').findall(key1[2::])
    k2 = re.compile('(..)').findall(key2[2::])
    if len(set(k1).intersection(set(k2))) == 0:
        combo = best_20[key1] + best_20[key2]
        if combo > best_permutation:
            best_permutation = combo
            print(f'\nbest_permutation')
print(best_permutation)
    
print(f'This took {datetime.now() - start}, ending at {datetime.now()}')