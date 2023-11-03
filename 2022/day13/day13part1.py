import json
def compare(left, right):
    if left == None:
        return True
    elif right == None:
        return False
    elif type(left) == list and type(right) == list:
        for i in range(max(len(left), len(right))):
            b = compare(get_list(left, i), get_list(right, i))
            if b: return True
            elif b == False: return False
    elif type(left) == list:
        return compare(left, [right])
    elif type(right) == list:
        return compare([left], right)
    elif left < right:
        return True
    elif right < left:
        return False

def get_list(l, i):
    try:
        return l[i]
    except IndexError:
        return None

correct = []
with open('./day13/day13j.txt', 'r') as f:
    l = [ json.loads(l.strip()) for l in f if l.strip() != '' ]
for i in range(len(l)//2):
    first_array = l[i * 2]
    second_array = l[i * 2 + 1]
    if i == 83:
        print(first_array, second_array)
    if compare(first_array, second_array):
        correct.append(i + 1)
print(correct)
print(sum(correct))
print(compare([[],[[[4],[5,3,8,5,8]],2],[9,6,10],[[[],0,2,[9,0,7,2]],[9,8],[],10,5],[5,[3]]], [[],[[[1,9,10],0]]]))
print(compare([[[],8,8,[]],[10,[10,[8,7],1,[5,9,9,1,7],4],5],[1,8,[5,1,[9,7,10,5],7],[[6,7],[8],[9],0,6],4]], [[[]],[[8,4],7,3,[]],[[],10,[5,[1],[8,3,2,1]]],[[[2,3,10,2]],4,1,4],[9,2]]))