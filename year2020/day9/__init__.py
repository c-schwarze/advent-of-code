def day9():
    with open("year2020/day9/input.txt", "r") as f:
        full_array = f.read().splitlines()
    full_array = turn_to_ints(full_array)

    print('Part 1 - Find the first number that doesnt work')
    print(part1(full_array))
    print('Part 2 - ')
    print(part2(full_array))


# answer = 18272118
def part1(full_array):
    preamble = full_array[0:25]
    new_full_array = full_array[25:]
    for check_num in new_full_array:
        if do_numbers_work(check_num, preamble):
            preamble.pop(0)
            preamble.append(check_num)
        else:
            return check_num

    return 'couldnt find a bad number'

# answer = 2186361
def part2(full_array):
    invalid_number = part1(full_array)
    start_index = 0
    while start_index < len(full_array):
        added_numbers = []
        current_total = 0
        for num in full_array[start_index:full_array.index(invalid_number)+1]:
            current_total += num
            added_numbers.append(num)
            if current_total == invalid_number:
                added_numbers.sort()
                return added_numbers[0] + added_numbers[-1]
            elif num == invalid_number:
                break
        start_index += 1

    return 'todo'


def do_numbers_work(check_num, preamble):
    for num1 in preamble:
        for num2 in preamble:
            if num1 != num2 and check_num == (num1 + num2):
                return True
    return False


def turn_to_ints(full_array):
    new_full_array = []
    for num in full_array:
        new_full_array.append(int(num))

    return new_full_array