import json
import functools

def cmp(left, right):
    if left == None:
        return True
    elif right == None:
        return False
    elif type(left) == list and type(right) == list:
        for i in range(max(len(left), len(right))):
            b = cmp(get_list(left, i), get_list(right, i))
            if b != None:
                return b
    elif type(left) == list:
        return cmp(left, [right])
    elif type(right) == list:
        return cmp([left], right)
    elif left < right:
        return True
    elif right < left:
        return False

def list_cmp(left, right):
    if cmp(left, right):
        return -1
    elif cmp(left, right) == False:
        return 1
    else:
        return 0
    

def get_list(l, i):
    try:
        return l[i]
    except IndexError:
        return None

with open('./day13/day13input.txt', 'r') as f:
    l = [ json.loads(l.strip()) for l in f if l.strip() != '' ]
    l.append([[2]])
    l.append([[6]])
l.sort(key=functools.cmp_to_key(list_cmp))
print(l)
print(l.index([[2]]))
print(l.index([[6]]))