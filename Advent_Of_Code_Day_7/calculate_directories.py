
class DirectoryReader:
    def __init__(self, directory_array):
        self.directory_array = directory_array
        self.directory_changes = []
        self.root_size = 0

        with open("device_directory.txt") as f:
            for line in f:
                line = line.strip('\n')
                directory_array.append(line)
            # print(directory_array)
            # for idx, command in enumerate(directory_array):
            #     print(command)

    def find_directory_changes(self):
        for idx, command in enumerate(self.directory_array):
            if command[0:4] == '$ cd' and command != '$ cd ..':
                self.directory_changes.append(idx)
        # print(self.directory_changes)

    def find_directory_totals(self):
        total = 0
        current_directory = []
        for idx, command in enumerate(self.directory_array):
            # print(command)
            if command[0:4] == '$ cd' and command != '$ cd ..':
                current_directory.append(command[5:])
                # print(current_directory[len(current_directory) - 1], total)
                print(current_directory, total)
            if command == '$ cd ..':
                remove_index = len(current_directory) - 1
                del current_directory[remove_index]
                # print(current_directory[len(current_directory) - 1], total)
                print(current_directory, total)
            if command[0:1] != '$' and command[0:3] != 'dir':
                end_char = command.find(' ') + 1
                file_size = command[0:end_char]
                total += int(file_size)
            if idx == len(self.directory_array) - 1:
                print(current_directory, total)

    def get_directory_amounts(self):
        total = 0
        new_total = 0
        current_directory = []
        for value in self.directory_changes:
            # print(value)
            for idx, command in enumerate(self.directory_array[value:]):
                if command[0:4] == '$ cd' and command != '$ cd ..':
                    current_directory.append(command[5:])
                if command == '$ cd ..':
                    check_val = self.directory_array[value]
                    if current_directory[len(current_directory) - 1] == check_val[5:]:
                        # print(current_directory, total)
                        break
                    else:
                        remove_index = len(current_directory) - 1
                        del current_directory[remove_index]

                    # print(current_directory[len(current_directory) - 1], total)
                    # print(current_directory, total)
                if command[0:1] != '$' and command[0:3] != 'dir':
                    end_char = command.find(' ') + 1
                    file_size = command[0:end_char]
                    total += int(file_size)
            # print(self.directory_array[value], total)
            if self.directory_array[value] == '$ cd /':
                self.root_size = total
            if 550000 > total >= 528671:
                print(self.directory_array[value], total)
                new_total += total
            current_directory = []
            total = 0
        # print(new_total)
