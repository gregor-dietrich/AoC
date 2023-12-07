import os

last_day = 0
for file in [f for f in os.listdir() if os.path.isfile(f)]:
    if not file.startswith("day") or not file.endswith(".py"):
        continue
    day_number = int(file.split(".")[0][3:])
    last_day = day_number if day_number > last_day else last_day
next_filename = f"day{last_day + 1}"

with open(f"{next_filename}.py", "w", encoding="utf-8") as file:
    file.write(f'with open("inputs/{next_filename}.txt") as file:\n')
    file.write('\tfor line in file:\n')
    file.write('\t\tpass\n')
with open(f"inputs/{next_filename}.txt", "w", encoding="utf-8"):
    pass
