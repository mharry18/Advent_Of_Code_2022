pair_count = 0

with open("elf_clean_assignments.txt") as f:
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        comparison_1 = line[0].split('-')
        comparison_2 = line[1].split('-')
        if int(comparison_2[0]) >= int(comparison_1[0]) and int(comparison_2[1]) <= int(comparison_1[1]):
            pair_count += 1
        elif int(comparison_1[0]) >= int(comparison_2[0]) and int(comparison_1[1]) <= int(comparison_2[1]):
            pair_count += 1
        # else:
        #     print(comparison_1, comparison_2, "Not in range")


print(pair_count)


total_overlapping_pairs = 0
non_overlapping_sets = 0

with open("elf_clean_assignments.txt") as f:
    for line in f:
        line = line.strip('\n')
        line = line.split(',')
        comparison_1 = line[0].split('-')
        comparison_2 = line[1].split('-')
        if int(comparison_2[0]) >= int(comparison_1[0]) and int(comparison_2[1]) <= int(comparison_1[1]):
            total_overlapping_pairs += 1
        elif int(comparison_1[0]) >= int(comparison_2[0]) and int(comparison_1[1]) <= int(comparison_2[1]):
            total_overlapping_pairs += 1
        elif (
                (int(comparison_2[0]) <= int(comparison_1[0]) <= int(comparison_2[1])) or
                (int(comparison_1[0]) <= int(comparison_2[1]) <= int(comparison_1[1])) or
                (int(comparison_1[0]) <= int(comparison_2[0]) <= int(comparison_1[1])) or
                (int(comparison_2[0]) <= int(comparison_1[1]) <= int(comparison_2[1]))
        ):
            total_overlapping_pairs += 1
        else:
            non_overlapping_sets += 1
print(total_overlapping_pairs)
