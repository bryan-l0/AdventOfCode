class Counter(dict):
    def __missing__(self, key):
        return 0
with open('./day7/day7input.txt', 'r') as f:
    size = 0
    directory = Counter()
    tree = []
    total = 0
    for l in f:
        l = l.strip()
        if "$ cd .." == l:
            tree.pop()
            oldDir, currentDir = currentDir, '/'.join(tree)
            directory[currentDir] += directory[oldDir]
            continue
        if "$ cd" in l:
            tree.append(l.split()[2])
            currentDir = '/'.join(tree)
            directory[currentDir]
            continue
        left = l.split()[0]
        if left.isdigit(): directory[currentDir] += int(left)
while len(tree) > 1:
    tree.pop()
    oldDir, currentDir = currentDir, '/'.join(tree)
    directory[currentDir] += directory[oldDir]
minimum, target = 70_000_000, -(70_000_000 - 48_381_165 - 30_000_000)
for i in directory.values():
    if i > target:
        minimum = min(minimum, i)
print(minimum)