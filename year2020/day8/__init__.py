def day8():
    with open("year2020/day8/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print('Part 1 - Before running a 2nd time, what is in accumulator?')
    print(part1(full_array))
    print('Part 2 - Find the nop/jmp update, what is the accumulator at?')
    print(part2(full_array))


# answer = 1521
def part1(full_array):
    accumulator = 0
    current_index = 0
    indexes_hit = []
    while True:
        command, action = get_command(full_array[current_index])
        if current_index in indexes_hit:
            return accumulator
        indexes_hit.append(current_index)

        if command == 'acc':
            current_index += 1
            accumulator += int(action)
        elif command == 'jmp':
            current_index += int(action)
        elif command == 'nop':
            current_index += 1
        else:
            return 'ERROR!'


# answer = 1016
def part2(full_array):
    flip_index = 0
    while flip_index < len(full_array):
        new_full_array = full_array.copy()
        new_command, test_action = get_command(new_full_array[flip_index])

        if new_command == 'jmp':
            new_full_array[flip_index] = new_full_array[flip_index].replace('jmp', 'nop')
        elif new_command == 'nop':
            new_full_array[flip_index] = new_full_array[flip_index].replace('nop', 'jmp')
        else:
            flip_index += 1
            continue

        result = part2_run_through(new_full_array)
        if result is not False:
            return result

        flip_index += 1

    return 'did not find it....'


def part2_run_through(new_full_array):
    accumulator = 0
    current_index = 0
    indexes_hit = []
    while len(new_full_array) not in indexes_hit:
        try:
            command, action = get_command(new_full_array[current_index])
        except IndexError:
            return accumulator

        if current_index in indexes_hit:
            return False
        indexes_hit.append(current_index)

        if command == 'acc':
            current_index += 1
            accumulator += int(action)
        elif command == 'jmp':
            current_index += int(action)
        elif command == 'nop':
            current_index += 1
        else:
            return 'ERROR!'

    return accumulator


def get_command(line):
    line_split = line.split(' ')
    command = line_split[0]
    action = line_split[1]
    return command, action