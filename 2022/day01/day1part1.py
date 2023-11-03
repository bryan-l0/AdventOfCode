maximum, count = 0, 0
with open('day1input.txt', 'r') as f:
	for line in f:
		line = line.strip()
		if line == '': count, maximum = 0, max(maximum, count)
		else: count += int(line)
print(maximum)