file_name = "day1\input.txt"

col1 = []
col2 = []

with open(file_name, "r") as file:
    for line in file:
        c1, c2 = map(int, line.split())
        col1.append(c1)
        col2.append(c2)

col1.sort()
col2.sort()

differences = [abs(c1 - c2) for c1, c2 in zip(col1, col2)]
total_difference = sum(differences)

print("Sum of Differences:", total_difference)    #2430334


## Part 2 - Similarity Score

total_similarity = 0
for num in col1:
    col2_occurences = col2.count(num)
    total_similarity += num * col2_occurences

print("Sum of Similarity :",total_similarity)  #28786472