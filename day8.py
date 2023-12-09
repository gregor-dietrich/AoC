instructions, node_map, current_node, current_nodes, steps = None, {}, "AAA", [], 0
with open("inputs/day8.txt") as file:
	for line in file:
		if line.strip() == "":
			continue
		if instructions is None:
			instructions = line.strip()
			continue
		node_map[line[:3]] = [line[7:10], line[12:15]]
		if line[2] == "A":
			current_nodes.append(line[:3])

# Part 1
while current_node != "ZZZ":
	for i in range(len(instructions)):
		if current_node == "ZZZ":
			break
		steps += 1
		current_node = node_map[current_node][1] if instructions[i] == "R" else node_map[current_node][0]
		i = 0 if i == len(instructions) - 1 else i
print(steps)


# Part 2
def goal_reached() -> bool:
	for node in current_nodes:
		if node[2] != "Z":
			return False
	return True


steps, i = 0, 0
while not goal_reached():
	steps += 1
	for j in range(len(current_nodes)):
		current_nodes[j] = node_map[current_nodes[j]][1] if instructions[i] == "R" else node_map[current_nodes[j]][0]
	i = 0 if i == len(instructions) - 1 else i + 1
print(steps)
