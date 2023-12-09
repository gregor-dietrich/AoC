def sequence_finished(seq) -> bool:
	for item in seq:
		if item != 0:
			return False
	return True


sum_of_next_values, sum_of_previous_values = 0, 0
with open("inputs/day9.txt") as file:
	for line in file:
		sequences = [[int(n) for n in line.strip().split()]]
		while not sequence_finished(sequences[-1]):
			next_sequence = []
			for i in range(1, len(sequences[-1])):
				next_sequence.append(sequences[-1][i] - sequences[-1][i - 1])
			sequences.append(next_sequence)
		next_value, previous_value = 0, sequences[0][0]
		for sequence in sequences:
			next_value += sequence[-1]
		for i in range(1, len(sequences) - 1)[::-1]:
			previous_value = sequences[i - 1][0] - sequences[i][0]
			sequences[i - 1].insert(0, sequences[i - 1][0] - sequences[i][0])
		sum_of_next_values += next_value
		sum_of_previous_values += previous_value
		sequences[0].append(next_value)
print(sum_of_next_values)
print(sum_of_previous_values)
