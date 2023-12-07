# Part 1
with open("inputs/day6.txt") as file:
	data = []
	for line in file:
		line = line[11:].strip()
		while "  " in line:
			line = line.replace("  ", " ")
		data.append([int(x) for x in line.split()])

product_of_options = 1
for i in range(len(data[0])):
	options = 0
	for j in range(data[0][i]):
		if j * (data[0][i] - j) > data[1][i]:
			options += 1
	product_of_options *= options
print(product_of_options)

# Part 2
with open("inputs/day6.txt") as file:
	data = []
	for line in file:
		data.append(int(line[11:].strip().replace(" ", "")))

number_of_options = 0
for i in range(data[0]):
	if i * (data[0] - i) > data[1]:
		number_of_options += 1
print(number_of_options)
