

elf_rps_list = []

with open("RPS_Results.txt") as f:
    for item in f:
        elf_rps_list.append(item.strip('\n'))


def get_first_round_score():
    a_results = [['A X', 'Draw', 3, 1],
                 ['A Y', 'Win', 6, 2],
                 ['A Z', 'Loss', 0, 3]]
    b_results = [['B X', 'Loss', 0, 1],
                 ['B Y', 'Draw', 3, 2],
                 ['B Z', 'Win', 6, 3]]
    c_results = [['C X', 'Win', 6, 1],
                 ['C Y', 'Loss', 0, 2],
                 ['C Z', 'Draw', 3, 3]]

    running_score = 0

    for elem in elf_rps_list:
        round_score = 0
        if elem.find('A') == 0:
            for result in a_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score

        elif elem.find('B') == 0:
            for result in b_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score

        elif elem.find('C') == 0:
            for result in c_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score
    print(running_score)


def get_second_round_score():
    a_results = [['A X', 'Loss', 0, 3],
                 ['A Y', 'Draw', 3, 1],
                 ['A Z', 'Win', 6, 2]]
    b_results = [['B X', 'Loss', 0, 1],
                 ['B Y', 'Draw', 3, 2],
                 ['B Z', 'Win', 6, 3]]
    c_results = [['C X', 'Loss', 0, 2],
                 ['C Y', 'Draw', 3, 3],
                 ['C Z', 'Win', 6, 1]]

    running_score = 0

    for elem in elf_rps_list:
        round_score = 0
        if elem.find('A') == 0:
            for result in a_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score

        elif elem.find('B') == 0:
            for result in b_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score

        elif elem.find('C') == 0:
            for result in c_results:
                if elem.replace(' ', '') == result[0].replace(' ', ''):
                    round_score = result[2] + result[3]
                    running_score += round_score
    print(running_score)

get_first_round_score()
get_second_round_score()

