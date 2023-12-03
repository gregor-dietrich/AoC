def extract_number(string: str, pos: int) -> int:
    result = ""
    while pos > 0 and string[pos - 1].isnumeric():
        pos -= 1
    while pos < len(string) and string[pos].isnumeric():
        result += string[pos]
        pos += 1
    return int(result)


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

            # Horizontal
            if i > 0:
                if previous_line[i - 1].isnumeric():
                    numbers.append(extract_number(previous_line, i - 1))
            if i < len(previous_line) - 1:
                if previous_line[i + 1].isnumeric():
                    numbers.append(extract_number(previous_line, i + 1))
            # Vertical
            if len(previous_previous_line) == len(previous_line) and previous_previous_line[i].isnumeric():
                numbers.append(extract_number(previous_previous_line, i))
            if len(line) == len(previous_line) and line[i].isnumeric():
                numbers.append(extract_number(line, i))
            # Diagonal
            if i > 1:
                if len(previous_previous_line) > 0 and previous_previous_line[i - 1].isnumeric() and \
                        previous_previous_line[i] == ".":
                    numbers.append(extract_number(previous_previous_line, i - 1))
                if line[i - 1].isnumeric() and line[i] == ".":
                    numbers.append(extract_number(line, i - 1))
            if i < len(previous_line) - 2:
                if previous_previous_line[i + 1].isnumeric() and previous_previous_line[i] == ".":
                    numbers.append(extract_number(previous_previous_line, i + 1))
                if line[i + 1].isnumeric() and line[i] == ".":
                    numbers.append(extract_number(line, i + 1))

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
            # Horizontal
            if i > 0:
                if previous_line[i - 1].isnumeric():
                    numbers.append(extract_number(previous_line, i - 1))
            if i < len(previous_line) - 1:
                if previous_line[i + 1].isnumeric():
                    numbers.append(extract_number(previous_line, i + 1))
            # Vertical
            if len(previous_previous_line) == len(previous_line) and previous_previous_line[i].isnumeric():
                numbers.append(extract_number(previous_previous_line, i))
            if len(line) == len(previous_line) and line[i].isnumeric():
                numbers.append(extract_number(line, i))
            # Diagonal
            if i > 1:
                if len(previous_previous_line) > 0 and previous_previous_line[i - 1].isnumeric() and \
                        previous_previous_line[i] == ".":
                    numbers.append(extract_number(previous_previous_line, i - 1))
                if line[i - 1].isnumeric() and line[i] == ".":
                    numbers.append(extract_number(line, i - 1))
            if i < len(previous_line) - 2:
                if previous_previous_line[i + 1].isnumeric() and previous_previous_line[i] == ".":
                    numbers.append(extract_number(previous_previous_line, i + 1))
                if line[i + 1].isnumeric() and line[i] == ".":
                    numbers.append(extract_number(line, i + 1))

            if len(numbers) == 2:
                ratios.append(numbers[0] * numbers[1])
            elif len(numbers) > 2:
                ratios.pop()

        previous_previous_line = previous_line
        previous_line = line

print(sum(ratios))
