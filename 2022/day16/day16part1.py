import copy
from datetime import datetime 

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

# Cached tunnel times
cache = {'XK': {'YH': 2, 'XS': 2, 'RA': 2, 'NM': 3, 'EA': 4, 'YP': 5, 'EI': 5, 'NU': 6, 'CX': 6, 'ZG': 6, 'WK': 7, 'QC': 7, 'NC': 8, 'MW': 8}, 'EI': {'RA': 3, 'MW': 3, 'XK': 5, 'EA': 5, 'XS': 6, 'YH': 7, 'NU': 7, 'CX': 7, 'ZG': 7, 'WK': 8, 'QC': 8, 'NM': 8, 'NC': 9, 'YP': 10}, 'CX': {'NU': 2, 'QC': 2, 'EA': 2, 'WK': 3, 'ZG': 4, 'RA': 4, 'NC': 5, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'EA': {'CX': 2, 'ZG': 2, 'RA': 2, 'NU': 4, 'QC': 4, 'NC': 4, 'XK': 4, 'EI': 5, 'XS': 5, 'WK': 5, 'YH': 6, 'NM': 7, 'MW': 8, 'YP': 9}, 'XS': {'XK': 2, 'RA': 3, 'YH': 4, 'EA': 5, 'NM': 5, 'EI': 6, 'NU': 7, 'CX': 7, 'ZG': 7, 'YP': 7, 'WK': 8, 'QC': 8, 'NC': 9, 'MW': 9}, 'NM': {'YH': 2, 'YP': 2, 'XK': 3, 'XS': 5, 'RA': 5, 'EA': 7, 'EI': 8, 'NU': 9, 'CX': 9, 'ZG': 9, 'WK': 10, 'QC': 10, 'NC': 11, 'MW': 11}, 'NC': {'ZG': 2, 'WK': 2, 'EA': 4, 'NU': 4, 'QC': 4, 'CX': 5, 'RA': 6, 'XK': 8, 'EI': 9, 'XS': 9, 'YH': 10, 'NM': 11, 'MW': 12, 'YP': 13}, 'MW': {'EI': 3, 'RA': 6, 'XK': 8, 'EA': 8, 'XS': 9, 'YH': 10, 'NU': 10, 'CX': 10, 'ZG': 10, 'WK': 11, 'QC': 11, 'NM': 11, 'NC': 12, 'YP': 13}, 'RA': {'XK': 2, 'EA': 2, 'EI': 3, 'XS': 3, 'YH': 4, 'NU': 4, 'CX': 4, 'ZG': 4, 'WK': 5, 'QC': 5, 'NM': 5, 'NC': 6, 'MW': 6, 'YP': 7}, 'NU': {'CX': 2, 'WK': 2, 'QC': 2, 'ZG': 3, 'EA': 4, 'NC': 4, 'RA': 4, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'YH': {'NM': 2, 'XK': 2, 'YP': 4, 'XS': 4, 'RA': 4, 'EA': 6, 'EI': 7, 'NU': 8, 'CX': 8, 'ZG': 8, 'WK': 9, 'QC': 9, 'NC': 10, 'MW': 10}, 'YP': {'NM': 2, 'YH': 4, 'XK': 5, 'XS': 7, 'RA': 7, 'EA': 9, 'EI': 10, 'NU': 11, 'CX': 11, 'ZG': 11, 'WK': 12, 'QC': 12, 'NC': 13, 'MW': 13}, 'ZG': {'NC': 2, 'EA': 2, 'NU': 3, 'WK': 4, 'CX': 4, 'RA': 4, 'QC': 5, 'XK': 6, 'EI': 7, 'XS': 7, 'YH': 8, 'NM': 9, 'MW': 10, 'YP': 11}, 'QC': {'NU': 2, 'WK': 2, 'CX': 2, 'NC': 4, 'EA': 4, 'RA': 5, 'ZG': 5, 'XK': 7, 'EI': 8, 'XS': 8, 'YH': 9, 'NM': 10, 'MW': 11, 'YP': 12}, 'WK': {'NU': 2, 'NC': 2, 'QC': 2, 'CX': 3, 'ZG': 4, 'RA': 5, 'EA': 5, 'XK': 7, 'EI': 8, 'XS': 8, 'YH': 9, 'NM': 10, 'MW': 11, 'YP': 12}, 'AA': {'RA': 2, 'NU': 2, 'WK': 3, 'QC': 3, 'CX': 3, 'XK': 4, 'EA': 4, 'NC': 5, 'ZG': 5, 'EI': 5, 'XS': 5, 'YH': 6, 'NM': 7, 'MW': 8, 'YP': 9}}
# cache = {'XKYH': 2, 'XKXS': 2, 'XKRA': 2, 'XKNM': 3, 'XKEA': 4, 'XKYP': 5, 'XKEI': 5, 'XKNU': 6, 'XKCX': 6, 'XKZG': 6, 'XKWK': 7, 'XKQC': 7, 'XKNC': 8, 'XKMW': 8, 'EIRA': 3, 'EIMW': 3, 'EIXK': 5, 'EIEA': 5, 'EIXS': 6, 'EIYH': 7, 'EINU': 7, 'EICX': 7, 'EIZG': 7, 'EIWK': 8, 'EIQC': 8, 'EINM': 8, 'EINC': 9, 'EIYP': 10, 'CXNU': 2, 'CXQC': 2, 'CXEA': 2, 'CXWK': 3, 'CXZG': 4, 'CXRA': 4, 'CXNC': 5, 'CXXK': 6, 'CXEI': 7, 'CXXS': 7, 'CXYH': 8, 'CXNM': 9, 'CXMW': 10, 'CXYP': 11, 'EACX': 2, 'EAZG': 2, 'EARA': 2, 'EANU': 4, 'EAQC': 4, 'EANC': 4, 'EAXK': 4, 'EAEI': 5, 'EAXS': 5, 'EAWK': 5, 'EAYH': 6, 'EANM': 7, 'EAMW': 8, 'EAYP': 9, 'XSXK': 2, 'XSRA': 3, 'XSYH': 4, 'XSEA': 5, 'XSNM': 5, 'XSEI': 6, 'XSNU': 7, 'XSCX': 7, 'XSZG': 7, 'XSYP': 7, 'XSWK': 8, 'XSQC': 8, 'XSNC': 9, 'XSMW': 9, 'NMYH': 2, 'NMYP': 2, 'NMXK': 3, 'NMXS': 5, 'NMRA': 5, 'NMEA': 7, 'NMEI': 8, 'NMNU': 9, 'NMCX': 9, 'NMZG': 9, 'NMWK': 10, 'NMQC': 10, 'NMNC': 11, 'NMMW': 11, 'NCZG': 2, 'NCWK': 2, 'NCEA': 4, 'NCNU': 4, 'NCQC': 4, 'NCCX': 5, 'NCRA': 6, 'NCXK': 8, 'NCEI': 9, 'NCXS': 9, 'NCYH': 10, 'NCNM': 11, 'NCMW': 12, 'NCYP': 13, 'MWEI': 3, 'MWRA': 6, 'MWXK': 8, 'MWEA': 8, 'MWXS': 9, 'MWYH': 10, 'MWNU': 10, 'MWCX': 10, 'MWZG': 10, 'MWWK': 11, 'MWQC': 11, 'MWNM': 11, 'MWNC': 12, 'MWYP': 13, 'RAXK': 2, 'RAEA': 2, 'RAEI': 3, 'RAXS': 3, 'RAYH': 4, 'RANU': 4, 'RACX': 4, 'RAZG': 4, 'RAWK': 5, 'RAQC': 5, 'RANM': 5, 'RANC': 6, 'RAMW': 6, 'RAYP': 7, 'NUCX': 2, 'NUWK': 2, 'NUQC': 2, 'NUZG': 3, 'NUEA': 4, 'NUNC': 4, 'NURA': 4, 'NUXK': 6, 'NUEI': 7, 'NUXS': 7, 'NUYH': 8, 'NUNM': 9, 'NUMW': 10, 'NUYP': 11, 'YHNM': 2, 'YHXK': 2, 'YHYP': 4, 'YHXS': 4, 'YHRA': 4, 'YHEA': 6, 'YHEI': 7, 'YHNU': 8, 'YHCX': 8, 'YHZG': 8, 'YHWK': 9, 'YHQC': 9, 'YHNC': 10, 'YHMW': 10, 'YPNM': 2, 'YPYH': 4, 'YPXK': 5, 'YPXS': 7, 'YPRA': 7, 'YPEA': 9, 'YPEI': 10, 'YPNU': 11, 'YPCX': 11, 'YPZG': 11, 'YPWK': 12, 'YPQC': 12, 'YPNC': 13, 'YPMW': 13, 'ZGNC': 2, 'ZGEA': 2, 'ZGNU': 3, 'ZGWK': 4, 'ZGCX': 4, 'ZGRA': 4, 'ZGQC': 5, 'ZGXK': 6, 'ZGEI': 7, 'ZGXS': 7, 'ZGYH': 8, 'ZGNM': 9, 'ZGMW': 10, 'ZGYP': 11, 'QCNU': 2, 'QCWK': 2, 'QCCX': 2, 'QCNC': 4, 'QCEA': 4, 'QCRA': 5, 'QCZG': 5, 'QCXK': 7, 'QCEI': 8, 'QCXS': 8, 'QCYH': 9, 'QCNM': 10, 'QCMW': 11, 'QCYP': 12, 'WKNU': 2, 'WKNC': 2, 'WKQC': 2, 'WKCX': 3, 'WKZG': 4, 'WKRA': 5, 'WKEA': 5, 'WKXK': 7, 'WKEI': 8, 'WKXS': 8, 'WKYH': 9, 'WKNM': 10, 'WKMW': 11, 'WKYP': 12, 'AARA': 2, 'AANU': 2, 'AAWK': 3, 'AAQC': 3, 'AACX': 3, 'AAXK': 4, 'AAEA': 4, 'AANC': 5, 'AAZG': 5, 'AAEI': 5, 'AAXS': 5, 'AAYH': 6, 'AANM': 7, 'AAMW': 8, 'AAYP': 9}

# History, Mapping, Time, Open Time
stack = [(['AA'], mapping_drop_no_flow(mapping), 1, {}, 0)]

maximum = -1
time = 31
flows = len(tunnels_with_flow())

while len(stack) > 0:
    current = stack.pop()
    key = current[0][-1]
    if current[4] == flows or current[2] > time:
        maximum = max(maximum, get_total_flow(current[3], time))
        continue
    if key in current[1]:
        current[3][key] = current[2] + 1
        current = (current[0], current[1], current[2] + 1, current[3], current[4])
        current[1].remove(key)
    if current[4] == flows or current[2] > time:
        maximum = max(maximum, get_total_flow(current[3], time))
        continue
    for k in current[1]:
        stack.append(((current[0] + [k]), copy.deepcopy(current[1]), current[2] + get_distance(key, k), copy.deepcopy(current[3]), current[4] + 1))
print(maximum)
print(f'This took {datetime.now() - start}, ending at {datetime.now()}')