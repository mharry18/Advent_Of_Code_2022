# test_case = 'mjpsHcssDzLTzMsz'
#
# print(len(test_case))
#
# print(len(test_case[0:8]))
import string

priority_total = 0
letter_list = list(string.ascii_lowercase + string.ascii_uppercase)

with open("elf_packing.txt") as f:
    for line in f:
        line = line.strip('\n')
        split_line_char = int(len(line)/2)
        compartment_a = line[0:split_line_char]
        compartment_b = line[split_line_char:]
        item = ''.join(set(compartment_a).intersection(compartment_b))

        for index, letter in enumerate(letter_list):
            if letter == item:
                priority_total += index + 1
                # print(f'The letter is {letter} and the priority is {index + 1}')
print(priority_total)

badge_elves = []
sub_badge = []

with open("elf_packing.txt") as f:
    for index, line in enumerate(f):
        index += 1
        line = line.strip('\n')
        if index % 3 != 0 or index == 0:
            sub_badge.append(line)
        if index % 3 == 0 and index != 0:
            sub_badge.append(line)
            badge_elves.append(sub_badge)
            sub_badge = []

round_2_priority_total = 0

for group in badge_elves:
    individual_a = group[0]
    individual_b = group[1]
    individual_c = group[2]
    inner_a = ''.join(set(individual_a).intersection(individual_b).intersection(individual_c))
    for index, letter in enumerate(letter_list):
        if letter == inner_a:
            round_2_priority_total += index + 1

print(round_2_priority_total)

