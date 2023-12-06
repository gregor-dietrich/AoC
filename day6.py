# Part 1
with open("inputs/day6.txt") as file:
	lines = []
	for line in file:
		line = line[11:].strip()
		while "  " in line:
			line = line.replace("  ", " ")
		lines.append([int(x) for x in line.split()])
product_of_options = 1
for i in range(len(lines[0])):
	options = []
	for j in range(lines[0][i]):
		if j * (lines[0][i] - j) > lines[1][i]:
			options.append(j)
	product_of_options *= len(options)
print(product_of_options)

# Part 2
number_of_options = 0
with open("inputs/day6.txt") as file:
	lines = []
	for line in file:
		line = line[11:].strip().replace(" ", "")
		lines.append(int(line))
for i in range(lines[0]):
	if i * (lines[0] - i) > lines[1]:
		number_of_options += 1
print(number_of_options)
