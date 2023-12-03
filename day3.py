from typing import List


def extract_number(string: str, pos: int) -> int:
    result = ""
    while pos > 0 and string[pos - 1].isnumeric():
        pos -= 1
    while pos < len(string) and string[pos].isnumeric():
        result += string[pos]
        pos += 1
    return int(result)


def find_numbers(numbers_list: List['int'], index: int, pre_pre_line: str, pre_line: str, current_line: str) -> None:
    # Horizontal
    if index > 0:
        if pre_line[index - 1].isnumeric():
            numbers_list.append(extract_number(pre_line, index - 1))
    if index < len(pre_line) - 1:
        if pre_line[index + 1].isnumeric():
            numbers_list.append(extract_number(pre_line, index + 1))
    # Vertical
    if len(pre_pre_line) == len(pre_line) and pre_pre_line[index].isnumeric():
        numbers_list.append(extract_number(pre_pre_line, index))
    if len(current_line) == len(pre_line) and current_line[index].isnumeric():
        numbers_list.append(extract_number(current_line, index))
    # Diagonal
    if index > 1:
        if len(pre_pre_line) > 0 and pre_pre_line[index - 1].isnumeric() and \
                pre_pre_line[index] == ".":
            numbers_list.append(extract_number(pre_pre_line, index - 1))
        if current_line[index - 1].isnumeric() and current_line[index] == ".":
            numbers_list.append(extract_number(current_line, index - 1))
    if index < len(pre_line) - 2:
        if pre_pre_line[index + 1].isnumeric() and pre_pre_line[index] == ".":
            numbers_list.append(extract_number(pre_pre_line, index + 1))
        if current_line[index + 1].isnumeric() and current_line[index] == ".":
            numbers_list.append(extract_number(current_line, index + 1))


# Part 1
with open("inputs/day3.txt", "r") as file:
    previous_line = ""
    previous_previous_line = ""
    numbers = []
    for line in file:
        line = line.strip()
        for i in range(len(previous_line)):
            char = previous_line[i]
            if char == "." or char.isnumeric():
                continue
            find_numbers(numbers, i, previous_previous_line, previous_line, line)
        previous_previous_line = previous_line
        previous_line = line
print(sum(numbers))

# Part 2
with open("inputs/day3.txt", "r") as file:
    previous_line = ""
    previous_previous_line = ""
    ratios = []
    for line in file:
        line = line.strip()
        for i in range(len(previous_line)):
            char = previous_line[i]
            if char != "*":
                continue
            numbers = []
            find_numbers(numbers, i, previous_previous_line, previous_line, line)
            if len(numbers) == 2:
                ratios.append(numbers[0] * numbers[1])
        previous_previous_line = previous_line
        previous_line = line
print(sum(ratios))
