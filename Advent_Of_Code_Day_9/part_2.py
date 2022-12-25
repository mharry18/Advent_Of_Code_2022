head_commands = []
rope_positions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_positions = []
recorded_positions = []

# Create a loop of the change and as it increments check if the tail is too far from the head. (Ex. If the head is at
# (5, 3) and the tail is at (4,1) then bring it over to 5 and up to 2 (5,2) but don't count the space at (5,1)

# [-7, 0] [-8, 2]



# 1, -2

def check_position(front_position: list, back_position: list, index):
    x_pos_difference = front_position[0] - back_position[0]
    y_pos_difference = front_position[1] - back_position[1]
    # print(x_pos_difference, y_pos_difference)
    if x_pos_difference < -1 and y_pos_difference >= 1:
        back_position[0] -= 1
        back_position[1] += 1
    elif x_pos_difference < -1 and y_pos_difference <= -1:
        back_position[0] -= 1
        back_position[1] -= 1
    elif x_pos_difference > 1 and y_pos_difference >= 1:
        back_position[0] += 1
        back_position[1] += 1
    elif x_pos_difference > 1 and y_pos_difference <= -1:
        back_position[0] += 1
        back_position[1] -= 1
    elif x_pos_difference <= -1 and y_pos_difference > 1:
        back_position[0] -= 1
        back_position[1] += 1
    elif x_pos_difference <= -1 and y_pos_difference < -1:
        back_position[0] -= 1
        back_position[1] -= 1
    elif x_pos_difference >= 1 and y_pos_difference > 1:
        back_position[0] += 1
        back_position[1] += 1
    elif x_pos_difference >= 1 and y_pos_difference < -1:
        back_position[0] += 1
        back_position[1] -= 1
    elif x_pos_difference < -1:
        back_position[0] -= 1
    elif x_pos_difference > 1:
        back_position[0] += 1
    elif y_pos_difference < -1:
        back_position[1] -= 1
    elif y_pos_difference > 1:
        back_position[1] += 1
    if index == 8:
        new_tail_position = (back_position[0], back_position[1])
        tail_positions.append(new_tail_position)

def start_part_2():

    with open("rope_path.txt") as f:
        for line in f:
            line = line.strip('\n')
            head_commands.append(line)
        for command in head_commands:
            command = command.split(' ')
            head_move = int(command[1])
            # print(head_position, tail_position)
            count = 0
            rope_position_head = rope_positions[0]
            while count < head_move:
                if command[0] == 'L':
                    rope_position_head[0] -= 1
                    for index, rope_location in enumerate(rope_positions):
                        if index == 9:
                            break
                        else:
                            check_position(rope_positions[index], rope_positions[index + 1], index)
                    # print(head_position, tail_position)

                if command[0] == 'R':
                    rope_position_head[0] += 1
                    for index, rope_location in enumerate(rope_positions):
                        if index == 9:
                            break
                        else:
                            check_position(rope_positions[index], rope_positions[index + 1], index)
                    # print(head_position, tail_position)

                if command[0] == 'U':
                    rope_position_head[1] += 1
                    for index, rope_location in enumerate(rope_positions):
                        if index == 9:
                            break
                        else:
                            check_position(rope_positions[index], rope_positions[index + 1], index)
                    # print(head_position, tail_position)

                if command[0] == 'D':
                    rope_position_head[1] -= 1
                    for index, rope_location in enumerate(rope_positions):
                        if index == 9:
                            break
                        else:
                            check_position(rope_positions[index], rope_positions[index + 1], index)
                    # print(head_position, tail_position
                count += 1
        print(len(tail_positions))
        distinct_positions = set(tail_positions)
        new_tail_positions = list(distinct_positions)
        print(len(new_tail_positions))
        # for pos in tail_positions:
        #     print(pos)



