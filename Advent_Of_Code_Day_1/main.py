from functools import reduce
import numpy as np

with open("Elf-Food") as f:
    lines = f.readlines()

# -------- Build lists for each elf's food and append to elves list ---------#

elves = []
elf = []

for line in lines:
    line = line.strip('\n')
    if line != '':
        elf.append(int(line))
    if line == '':
        elves.append(elf)
        elf = []

# ------- Calculate total calories of the elf w/ most food -------- #

calorie_total = []

for elf in elves:
    calories = reduce(lambda a, b: a + b, elf)
    calorie_total.append(calories)

calorie_total.sort(reverse=True)
top_elf_calorie = np.max(calorie_total)

# ------- Calculate total calories of the top 3 elves' food -------- #

top_3_elves = []
while len(top_3_elves) < 3:
    index = len(top_3_elves)
    top_3_elves.append(calorie_total[index])

top_3_calories_total = reduce(lambda a, b: a + b, top_3_elves)

# -------- Return solution to each problem ---------- #

# --------- Part 1 answer --------- #

print(f'Total calories of the elf with the most food: {top_elf_calorie} calories')

# --------- Part 2 answer --------- #

print(f'Total calories of the top 3 elves\' food: {top_3_calories_total} calories')
