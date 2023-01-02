def run():
    f = open("year2022/day7/input.txt", "r")
    lines = []
    for x in f:
        lines.append(x.strip())

    print("--- PART 1 ---")
    print("Sum of all directories less than 100,000: ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("size of the file to delete to get under 30,000,000 size: ")
    print(part2(lines))


# answer = 2031851
def part1(lines):
    main_directory = build_tree(lines)
    main_directory_size = 0
    if main_directory.size <= 100000:
        main_directory_size = main_directory.size
    return recurse_sum_sizes_100000(main_directory) + main_directory_size

# answer = 2568781
def part2(lines):
    main_directory = build_tree(lines)

    amount_to_delete = main_directory.size - 40000000

    # we need to loop over every directory to find one that is the lowest, but 0 or greater of `dir - amount_to_delete`
    print("amount_to_delete = {}".format(amount_to_delete))
    result = recurse_find_smallest_dir_over_limit(main_directory, amount_to_delete)
    return result

def build_tree(lines):
    main_directory = Directory('', '/', [])
    current_directory = main_directory
    current_command = ''
    for line in lines:
        # command - cd
        if '$ cd' in line:
            # Not really applicable, but it follows the same guidelines
            current_command = 'cd'
            # TODO - the strip initially was causing issues with the $.
            param = line.split('$ cd ')[1]
            # base case
            if param == '/':
                current_directory = main_directory
                continue

            if param == '..':
                current_directory = current_directory.parent
                continue

            # check if directory exists
            found_directory = False
            for directory in current_directory.children:
                if directory.name == param and directory.type == 'dir':
                    found_directory = True
                    current_directory = directory
                    break

            if not found_directory:
                current_directory.children.append(Directory(current_directory, param, []))

        # command - ls
        elif '$ ls' in line:
            current_command = 'ls'
            continue

        # command output (only from ls)
        else:
            param1, param2 = line.split(' ')
            if param1 == 'dir':
                # param2 = name
                current_directory.children.append(Directory(current_directory, param2, []))
            else:
                # param1 = size
                # param2 = name
                current_directory.children.append(File(param2, param1))

    # this needs to update in place to update sizes
    recurse_update_dir_sizes(main_directory)

    return main_directory


class Directory():
    def __init__(self, parent, name, children):
        self.parent = parent
        self.name = name
        self.children = children
        self.type = 'dir'
        self.size = 0


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        self.type = 'file'


def recurse_update_dir_sizes(directory):
    for child in directory.children:
        if child.type == 'file':
            directory.size += child.size
        else:  # directory
            directory.size += recurse_update_dir_sizes(child)

    return directory.size

def recurse_sum_sizes_100000(directory):
    running_total = 0
    for child in directory.children:
        if child.type == 'dir':
            running_total += recurse_sum_sizes_100000(child)

    if directory.size <= 100000:
        running_total += directory.size

    return running_total


def recurse_find_smallest_dir_over_limit(directory, amount_to_delete):
    current_lowest = 99999999999
    for child in directory.children:
        if child.type == 'dir':
            # Check if the current directory is lowest
            if child.size >= amount_to_delete and child.size < current_lowest:
                current_lowest = child.size

            # check if recursing the directory finds the lowest
            child_lowest = recurse_find_smallest_dir_over_limit(child, amount_to_delete)
            if child_lowest < current_lowest:
                current_lowest = child_lowest

    if directory.size >= amount_to_delete and directory.size < current_lowest:
        current_lowest = directory.size

    return current_lowest
