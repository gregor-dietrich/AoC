import os

last_day = 0
for file in os.listdir():
    if not os.path.isfile(file):
        continue
    if not file.startswith("day") or not file.endswith(".py"):
        continue
    day_number = int(file.split(".")[0][3:])
    last_day = day_number if day_number > last_day else last_day
next_filename = f"day{last_day + 1}"

with open(f"{next_filename}.py", "w", encoding="utf-8"):
    pass
with open(f"inputs/{next_filename}.txt", "w", encoding="utf-8"):
    pass
