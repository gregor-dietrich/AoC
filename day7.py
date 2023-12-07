from multiprocessing import Pool
from typing import List, Callable, Any


def convert_values(s: str, part: int) -> List['int']:
	result = []
	faces = "123456789TJQKA" if part == 1 else "J23456789TQKA"
	for c in s:
		result.append(faces.find(c) if c in faces else int(c))
	return result


def calculate_rank(s: str) -> int:
	triples, pairs, seen_faces, cards = 0, 0, [], s
	for card in cards:
		if card in seen_faces:
			continue
		seen_faces.append(card)
		if cards.count(card) == 5:
			return 0
		elif cards.count(card) == 4:
			return 1
		elif cards.count(card) == 3:
			triples += 1
		elif cards.count(card) == 2:
			pairs += 1
	if triples == 1:
		if pairs == 1:
			return 2
		if pairs == 0:
			return 3
	if triples == 0:
		if pairs == 2:
			return 4
		if pairs == 1:
			return 5
	return 6


def replace_jokers(s: str) -> str:
	if "J" not in s:
		return s
	result, max_rank = s, calculate_rank(s)
	replacements = [s.replace("J", face) for face in "23456789TQKA"]
	for candidate in replacements:
		rank = calculate_rank(candidate)
		if rank == 0:
			return candidate
		if rank < max_rank:
			max_rank = rank
			result = candidate
	return result


def main(part=1):
	ranked_sets = [[], [], [], [], [], [], []]
	with open("inputs/day7.txt") as file:
		for line in file:
			hand, bid = line.split()[0], int(line.split()[1])
			rank = calculate_rank(hand if part == 1 else replace_jokers(hand))
			key_function: Callable[[Any], list[int]] = lambda x: [convert_values(card, part)[0] for card in x]
			for i, existing_hand_bid in enumerate(ranked_sets[rank]):
				if key_function(hand) > key_function(existing_hand_bid[0]):
					ranked_sets[rank].insert(i, [hand, bid])
					break
			else:
				ranked_sets[rank].append([hand, bid])
	total_score, rank_multiplier = 0, 0
	for ranked_set in ranked_sets[::-1]:
		for hand in ranked_set[::-1]:
			rank_multiplier += 1
			total_score += hand[1] * rank_multiplier
	print(f"Part {part}: {total_score}")


if __name__ == "__main__":
	with Pool(2) as p:
		p.map(main, [1, 2])
