message_code = []
letter_index = 0

with open("comm_codes.txt") as f:
    for line in f:
        line = line.strip('\n')
        # print(len(line))
        total_check = []
        sub_check = []
        print(line[1348:1352])
        print(line[1352:1356])


        while letter_index < 4095:
            # print(letter_index)
            search_range_start = letter_index
            search_range_finish = letter_index + 14
            code_list = line[search_range_start:search_range_finish]
            for index, code in enumerate(code_list):
                for check_index, check_code in enumerate(code_list):
                    # print(code, check_code)
                    if index == check_index:
                        continue
                    if code != check_code:
                        pass
                    if code == check_code:
                        sub_check.append("True")
            total_check.append(sub_check)
            sub_check = []
            # print("Check Done")




                # print(code_list)
                # print(code)



            # if line[letter_index] in line[search_range_start:search_range_finish]:
            #     pass
            # else:
            #     print("False")
            #     print(letter_index)

            # for letter in line[0:letter_index]:
            #     print(letter)
            letter_index += 1
            # print(letter_index)
        # print(total_check)
        for index, check in enumerate(total_check):
            if len(check) == 0:
                print(index + 14)
                break
