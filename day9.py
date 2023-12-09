def process_sequences(main_sequence: str) -> (int, int):
	sequences = [[int(val) for val in main_sequence.strip().split()]]
	while not all(item == 0 for item in sequences[-1]):
		sequences.append([sequences[-1][i] - sequences[-1][i - 1] for i in range(1, len(sequences[-1]))])
	next_val, previous_val = 0, sequences[0][0]
	for i in range(1, len(sequences))[::-1]:
		next_val += sequences[i - 1][-1]
		previous_val = sequences[i - 1][0] - sequences[i][0]
		sequences[i - 1].insert(0, sequences[i - 1][0] - sequences[i][0])
	return next_val, previous_val


sum_of_next_values, sum_of_previous_values = 0, 0
with open("inputs/day9.txt") as file:
	for line in file:
		next_value, previous_value = process_sequences(line)
		sum_of_next_values += next_value
		sum_of_previous_values += previous_value
print("%s\n%s" % (sum_of_next_values, sum_of_previous_values))
