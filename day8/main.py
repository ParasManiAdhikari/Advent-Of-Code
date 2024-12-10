from itertools import combinations
import sys
from collections import defaultdict

file_name = "day8\ex.txt"

with open(file_name, "r") as file:
    lines = list(map(str.strip, file.readlines()))

antenna = defaultdict(set)

for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != '.':
            antenna[val].add((r,c))


antinodes = set()

for freq in antenna:
    for (r1, c1), (r2, c2) in combinations(antenna[freq], 2):
        antinodes.add((2*r1 - r2, 2*c1-c2))
        antinodes.add((2*r2 - r1, 2*c2-c1))

num_rows = len(lines)
num_cols = len(lines[0])
part1 = sum(1 for r,c in antinodes if 0 <= r < num_rows and 0 <= c < num_cols)
print(part1)

# Part 2