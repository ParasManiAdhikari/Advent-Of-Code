file_name = "day9\input.txt"

with open(file_name, "r") as file:
    lines = list(map(int, file.read().strip()))

disk = []
for i in range(0, len(lines), 2):
    disk.extend(lines[i]*[i // 2])
    if i + 1 < len(lines):
        disk.extend(lines[i+1] * [-1])

empty_ids = [i for i, val in enumerate(disk) if val == -1]

# re-order
i = 0
while True:
    while disk[-1] == -1 : disk.pop()
    target = empty_ids[i]
    if target >= len(disk):
        break
    disk[target] = disk.pop()
    i += 1

#checksum
cs = sum(i*val for i, val in enumerate(disk))
print(cs)