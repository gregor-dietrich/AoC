instructions, node_map, first = None, {}, True
with open("inputs/day8.txt") as file:
	for line in file:
		if line.strip() == "":
			continue
		if first:
			instructions = line.strip()
			first = False
			continue
		node_map[line[:3]] = [line[7:10], line[12:15]]
steps, current_node = 0, "AAA"
while current_node != "ZZZ":
	for i in range(len(instructions)):
		if current_node == "ZZZ":
			break
		steps += 1
		current_node = node_map[current_node][1] if instructions[i] == "R" else node_map[current_node][0]
		if i == len(instructions) - 1:
			i = 0
print(steps)
