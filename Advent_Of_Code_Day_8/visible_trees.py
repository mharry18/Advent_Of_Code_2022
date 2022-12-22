working_forest = []
visible_trees = []

def check_left(tree, idx, pos):
    final_index = len(working_forest[idx][:pos]) - 1
    forest_loop = list(reversed(working_forest[idx][:pos]))
    for index, tree_neighbor in enumerate(forest_loop):
        if tree_neighbor < tree and final_index != index:
            continue
        elif tree_neighbor < tree and final_index == index:
            return True
        else:
            # print("Not Visible")
            return False


def check_right(tree, idx, pos):
    final_index = len(working_forest[idx][pos + 1:]) - 1
    forest_loop = list(working_forest[idx][pos + 1:])
    for index, tree_neighbor in enumerate(forest_loop):
        if tree_neighbor < tree and final_index != index:
            continue
        elif tree_neighbor < tree and final_index == index:
            return True
        else:
            # print("Not Visible")
            return False


def check_up(tree, tree_row_look_back):
    while tree_row_look_back >= 0:
        tree_neighbor = working_forest[tree_row_look_back][pos]
        # print(tree_neighbor)
        if tree_neighbor < tree and tree_row_look_back != 0:
            tree_row_look_back -= 1
        elif tree_neighbor < tree and tree_row_look_back == 0:
            return True
        else:
            # print("Not Visible")
            return False


def check_down(tree, tree_row_look_ahead):
    while tree_row_look_ahead < len(working_forest):
        tree_neighbor = working_forest[tree_row_look_ahead][pos]
        # print(tree_neighbor)
        if tree_neighbor < tree and tree_row_look_ahead != len(working_forest) - 1:
            tree_row_look_ahead += 1
        elif tree_neighbor < tree and tree_row_look_ahead == len(working_forest) - 1:
            return True
        else:
            # print("Not Visible")
            return False


def check_tree_array(tree, pos, idx):
    # LOOKING LEFT TO GRID OF CURRENT TREE #
    # print(tree)
    tree_row_look_back = idx - 1
    # print(tree_row_look_back)
    tree_row_look_ahead = idx + 1
    # print(tree_row_look_ahead)
    check_pos = pos
    if check_left(tree, idx, check_pos):
        return True
    else:
        if check_right(tree, idx, check_pos):
            return True
        else:
            if check_up(tree, tree_row_look_back):
                return True
            else:
                if check_down(tree, tree_row_look_ahead):
                    return True
                else:
                    return False


with open("forest_map.txt") as f:
    for idx, line in enumerate(f):
        line = line.strip('\n')
        working_forest.append(line)
    # print(working_forest)

    for idx, row in enumerate(working_forest):
        # VISIBLE TREES (ON THE EDGE OF THE GRID) #
        if idx == 0 or idx == len(working_forest) - 1:
            for t in row:
                visible_trees.append(t)
            # print(visible_trees)
            # print(idx, 0, len(working_forest) - 1)
        else:
            # print(idx, 0, len(working_forest) - 1)
            for pos, tree in enumerate(row):
                # print(tree, pos)
                # VISIBLE TREES (ON THE EDGE OF THE GRID) #
                if pos == 0 or pos == len(row) - 1:
                    visible_trees.append(tree)
                    # print(visible_trees)
                    # print(0, len(row) - 1)
                else:
                    # print(tree, pos)
                    if check_tree_array(tree, pos, idx):
                        visible_trees.append(tree)
                        continue
                    else:
                        continue
    print(visible_trees)
    print(len(visible_trees))