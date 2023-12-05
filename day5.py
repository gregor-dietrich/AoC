from datetime import datetime

data = {}


def seed_to_location(seed: int) -> int:
    soil = lookup_data(seed, "seed-to-soil")
    fertilizer = lookup_data(soil, "soil-to-fertilizer")
    water = lookup_data(fertilizer, "fertilizer-to-water")
    light = lookup_data(water, "water-to-light")
    temperature = lookup_data(light, "light-to-temperature")
    humidity = lookup_data(temperature, "temperature-to-humidity")
    location = lookup_data(humidity, "humidity-to-location")
    return location


def lookup_data(key: int, data_type: str = "") -> int:
    for source_start in data[data_type]:
        if key < source_start or key > source_start + data[data_type][source_start][1] - 1:
            continue
        destination_start = data[data_type][source_start][0]
        # print(f"Lookup: Key={key}, Data={data_type}, Result={destination_start + key - source_start}")
        return destination_start + key - source_start
    # print(f"Lookup: Key={key}, Data={data_type}, Result={key}")
    return key


with open("inputs/day5.txt", "r") as input_file:
    current_key = ""
    for line in input_file:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("seeds: "):
            line = line[7:].split()
            data["seeds"] = [int(seed) for seed in line]
            continue
        if line[0].isnumeric():
            values = [int(value) for value in line.split()]
            data[current_key][values[1]] = [values[0], values[2]]
            continue
        if current_key != "":
            data[current_key] = dict(sorted(data[current_key].items()))
        current_key = line[:-5]
        data[current_key] = {}

# Part 1
locations = []
for seed in data["seeds"]:
    locations.append(seed_to_location(seed))
print(min(locations))

# Part 2
nearest_location = float('inf')
for i in range(1, len(data["seeds"]), 2):
    start, end = int(data["seeds"][i - 1]), int(data["seeds"][i - 1]) + int(data["seeds"][i])
    nearest_location = min(nearest_location, min(seed_to_location(j) for j in range(start, end + 1)))
print(nearest_location)
