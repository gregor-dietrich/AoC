from typing import List


def count_matches(card_data: List['str']) -> int:
    matched = 0
    for guessed_number in set(card_data[0].strip().split()):
        if guessed_number in set(card_data[1].strip().split()):
            matched += 1
    return matched


# Part 1
total_score = 0
with open("inputs/day4.txt", "r") as file:
    score = 0
    for line in file:
        for i in range(count_matches(line.strip().split(": ")[1].split(" | "))):
            score = 1 if i == 0 else score * 2
        total_score += score
print(total_score)


# Part 2
cards = []
with open("inputs/day4.txt", "r") as file:
    for line in file:
        data = line.strip().split(": ")[1].split(" | ")
        cards.append([data[0].strip(), data[1].strip(), int(line.strip().split(": ")[0][5:].strip())])
for card in cards:
    for i in range(count_matches(card)):
        cards.append(cards[card[2] + i])
print(len(cards))
