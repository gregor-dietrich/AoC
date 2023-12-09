from typing import List


def sequence_finished(sequence: List['int']) -> bool:
	for item in sequence:
		if item != 0:
			return False
	return True


sum_of_next_values = 0
with open("inputs/day9.txt") as file:
	for line in file:
		sequences = [[int(n) for n in line.strip().split()]]
		while not sequence_finished(sequences[-1]):
			next_sequence = []
			for i in range(1, len(sequences[-1])):
				next_sequence.append(sequences[-1][i] - sequences[-1][i - 1])
			sequences.append(next_sequence)
		next_value = 0
		for sequence in sequences:
			next_value += sequence[-1]
		sum_of_next_values += next_value
print(sum_of_next_values)
