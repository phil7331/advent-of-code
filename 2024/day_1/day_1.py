group1 = []
group2 = []

with open("input.txt", "r") as file:
    for line in file:
        split_line = line.split()
        group1.append(int(split_line[0]))
        group2.append(int(split_line[1]))

group1.sort()
group2.sort()

distance = sum(abs(group1[i] - group2[i]) for i in range(len(group1)))

print(f"Solution: {distance}")
