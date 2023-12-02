# Read data
counts = []
with open("inputs/day2.txt", "r") as file:
    for line in file:
        game_round = [0, 0, 0]
        for draws in [[draw.strip() for draw in result.split(",")] for result in line.split(": ")[1].split(";")]:
            for draw in draws:
                color = draw.split()
                colors = ["red", "green", "blue"]
                for i in range(len(colors)):
                    if color[1] == colors[i]:
                        game_round[i] = max(game_round[i], int(color[0]))
        counts.append(game_round)

# Part 1
sum_of_ids = 0
max_counts = [12, 13, 14]
for i in range(len(counts)):
    valid = True
    for j in range(len(max_counts)):
        if counts[i][j] > max_counts[j]:
            valid = False
            break
    if valid:
        sum_of_ids += i + 1
print(sum_of_ids)

# Part 2
sum_of_powers = 0
for count in counts:
    sum_of_powers += count[0] * count[1] * count[2]
print(sum_of_powers)
