file_name = "day1\input.txt"

col1 = []
col2 = []

with open(file_name, "r") as file:
    for line in file:
        c1, c2 = map(int, line.split())
        col1.append(c1)
        col2.append(c2)

# print("Column 1:", col1)
# print("Column 2:", col2)

col1.sort()
col2.sort()

differences = [abs(c1 - c2) for c1, c2 in zip(col1, col2)]
total_difference = sum(differences)

# print("\nColumn 1 Sorted:", col1)
# print("Column 2 Sorted:", col2)
# print("\nDifferences (Row-wise):", differences)
print("Sum of Differences:", total_difference)    #2430334