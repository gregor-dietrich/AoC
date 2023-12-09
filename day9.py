def process_sequences(sequence: str) -> (int, int):
	sequence = [[int(n) for n in sequence.strip().split()]]
	while not all(item == 0 for item in sequence[-1]):
		next_sequence = []
		for i in range(1, len(sequence[-1])):
			next_sequence.append(sequence[-1][i] - sequence[-1][i - 1])
		sequence.append(next_sequence)
	next_val, previous_val = 0, sequence[0][0]
	for i in range(1, len(sequence))[::-1]:
		next_val += sequence[i - 1][-1]
		previous_val = sequence[i - 1][0] - sequence[i][0]
		sequence[i - 1].insert(0, sequence[i - 1][0] - sequence[i][0])
	return next_val, previous_val


sum_of_next_values, sum_of_previous_values = 0, 0
with open("inputs/day9.txt") as file:
	for line in file:
		next_value, previous_value = process_sequences(line)
		sum_of_next_values += next_value
		sum_of_previous_values += previous_value
print("%s\n%s" % (sum_of_next_values, sum_of_previous_values))
