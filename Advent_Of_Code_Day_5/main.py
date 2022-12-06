crate_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
count = 0
column_ref = 1
words_to_remove = ['move', ' from', ' to']

crate = []
sub_crate = []

while count < 9:
    with open("crate_commands.txt") as f:
        for line in f:
            try:
                line = line.strip('\n')
                if len(line) == 0:
                    break
                if line[column_ref] != " " and line[column_ref] not in crate_number:
                    sub_crate.append(line[column_ref])
            except IndexError:
                pass
            # print(line[0:3])
        crate.append(sub_crate)
        sub_crate = []
    column_ref += 4
    count += 1

count = 0
print(crate)

# ----------- Part 1 ------------ #


def crates_in_reversed_order():

    with open("crate_commands.txt") as f:
        for line in f:

            line = line.strip('\n')
            if line[0:4] == "move":
                for word in words_to_remove:
                    line = line.replace(word, "")
                line = line.strip(' ')
                line = line.split(' ')

                number_to_move = int(line[0])
                column_from = int(line[1]) - 1
                column_to = int(line[2]) - 1
                # print(number_to_move, column_from, column_to)
                boxes_to_move = crate[column_from][0:number_to_move]

                del crate[column_from][0:number_to_move]
                boxes_to_move.reverse()

                crate[column_to][0:0] = boxes_to_move
                boxes_to_move = []

                count += 1
            # print(crate)

    # for crate_column in crate:
    #     print(crate_column[0])


# ----------- PART 2 ------------ #


def crates_in_regular_order():
    count = 0

    with open("crate_commands.txt") as f:
        for line in f:

            line = line.strip('\n')
            if line[0:4] == "move":
                for word in words_to_remove:
                    line = line.replace(word, "")
                line = line.strip(' ')
                line = line.split(' ')

                number_to_move = int(line[0])
                column_from = int(line[1]) - 1
                column_to = int(line[2]) - 1
                # print(number_to_move, column_from, column_to)
                boxes_to_move = crate[column_from][0:number_to_move]

                del crate[column_from][0:number_to_move]

                crate[column_to][0:0] = boxes_to_move
                boxes_to_move = []

                count += 1
            # print(crate)

    answer = ''

    for crate_column in crate:
        answer = answer + crate_column[0]

    return answer


print(crates_in_regular_order())