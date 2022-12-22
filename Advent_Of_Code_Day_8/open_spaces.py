working_forest = []
scenic_scores = []

def scenic_score(a: int, b: int, c: int, d: int) -> int:
    return a * b * c * d

def check_left(tree, idx, pos):
    count = 0
    final_index = len(working_forest[idx][:pos]) - 1
    forest_loop = list(reversed(working_forest[idx][:pos]))
    for index, tree_neighbor in enumerate(forest_loop):
        count += 1
        if tree_neighbor >= tree:
            return count
        elif final_index == index:
            return count


def check_right(tree, idx, pos) -> int:
    count = 0
    final_index = len(working_forest[idx][pos + 1:]) - 1
    forest_loop = list(working_forest[idx][pos + 1:])
    for index, tree_neighbor in enumerate(forest_loop):
        count += 1
        if tree_neighbor >= tree:
            return count
        elif final_index == index:
            return count


def check_up(tree, tree_row_look_back, pos) -> int:
    count = 0
    while tree_row_look_back >= 0:
        count += 1
        tree_neighbor = working_forest[tree_row_look_back][pos]
        # print(tree_neighbor)
        if tree_neighbor >= tree:
            return count
        elif tree_row_look_back == 0:
            return count
        else:
            tree_row_look_back -= 1



def check_down(tree, tree_row_look_ahead, pos):
    count = 0
    while tree_row_look_ahead < len(working_forest):
        count += 1
        tree_neighbor = working_forest[tree_row_look_ahead][pos]
        # print(tree_neighbor)
        if tree_neighbor >= tree:
            return count
        elif tree_row_look_ahead == len(working_forest) - 1:
            return count
        else:
            tree_row_look_ahead += 1


def check_tree_array(tree, pos, idx):
    # LOOKING LEFT TO GRID OF CURRENT TREE #
    # print(tree)
    tree_row_look_back = idx - 1
    # print(tree_row_look_back)
    tree_row_look_ahead = idx + 1
    # print(tree_row_look_ahead)
    check_pos = pos
    position_1 = check_left(tree, idx, check_pos)
    position_2 = check_right(tree, idx, check_pos)
    position_3 = check_up(tree, tree_row_look_back, pos)
    position_4 = check_down(tree, tree_row_look_ahead, pos)
    return scenic_score(position_1, position_2, position_3, position_4)


def read_file():
    with open("forest_map.txt") as f:
        for idx, line in enumerate(f):
            line = line.strip('\n')
            working_forest.append(line)

        for idx, row in enumerate(working_forest):
            # VISIBLE TREES (ON THE EDGE OF THE GRID) #
            if idx == 0 or idx == len(working_forest) - 1:
                pass
                # print(visible_trees)
                # print(idx, 0, len(working_forest) - 1)
            else:
                # print(idx, 0, len(working_forest) - 1)
                for pos, tree in enumerate(row):
                    # print(tree, pos)
                    # VISIBLE TREES (ON THE EDGE OF THE GRID) #
                    if pos == 0 or pos == len(row) - 1:
                        pass
                        # print(visible_trees)
                        # print(0, len(row) - 1)
                    else:
                        print(tree, pos)
                        scenic_scores.append(check_tree_array(tree, pos, idx))
                        continue
        print(max(scenic_scores))