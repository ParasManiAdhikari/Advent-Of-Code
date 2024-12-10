file_name = "day9\ex.txt"

with open(file_name, "r") as file:
    lines = list(map(int, file.read().strip()))

file_sizes = lines[0::2]
free_space = lines[1::2]

print(lines)
print(file_sizes, free_space)
print(free_space)