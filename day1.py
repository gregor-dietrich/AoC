import re

# Part 1
total_sum = 0
with open("inputs/day1.txt", "r") as file:
    for line in file:
        digits = re.findall(r"\d", line)
        total_sum += int(digits[0] + digits[-1])
print(total_sum)

# Part 2
aliases = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
           "9": "nine"}
total_sum = 0
with open("inputs/day1.txt", "r") as file:
    for line in file:
        matches = {}
        for char in line:
            if char in aliases:
                for match in re.finditer(char, line):
                    matches[match.start()] = char
        for alias in aliases.keys():
            if aliases[alias] in line:
                for match in re.finditer(aliases[alias], line):
                    matches[match.start()] = alias
        numbers = dict(sorted(matches.items()))
        numbers = [numbers[number] for number in numbers]
        total_sum += int(numbers[0] + numbers[-1])
print(total_sum)
