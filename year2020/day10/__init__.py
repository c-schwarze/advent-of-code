def day10():
    with open("year2020/day10/input.txt", "r") as f:
        full_array = f.read().splitlines()

    int_array = []
    int_array.append(0)
    for num in full_array:
        int_array.append(int(num))
    int_array.sort()
    int_array.append(int_array[-1]+3)

    print('Part 1 - # of 1 jolt differences * # of 3 jolt differences')
    print(part1(int_array))
    print('Part 2 - # of combinations')
    print(part2(int_array))


# answer = 1848
def part1(full_array):
    index = 0
    one_difference_counter = 0
    three_difference_counter = 0

    for jolt in full_array:
        try:
            next_jolt = full_array[index+1]
        except:
            continue
        jolt_difference = next_jolt - jolt
        if jolt_difference == 1:
            one_difference_counter += 1
        elif jolt_difference == 3:
            three_difference_counter += 1
        index += 1

    return one_difference_counter * three_difference_counter


# answer = 8099130339328
def part2(full_array):
    return recursive_jolt_finder({}, full_array, 0)


def recursive_jolt_finder(cache_dict, full_array, index):
    try:
        if str(index) in cache_dict:
            return cache_dict[str(index)]
    except:
        pass
    current_jolt = full_array[index]
    next_jolt1 = 0
    next_jolt2 = 0
    next_jolt3 = 0
    if index + 1 >= len(full_array):
        cache_dict[str(index)] = 1
        return 1
    if index+1 < len(full_array) and full_array[index+1] - current_jolt <= 3:
        next_jolt1 = recursive_jolt_finder(cache_dict, full_array, index+1)
    if index+2 < len(full_array) and full_array[index+2] - current_jolt <= 3:
        next_jolt2 = recursive_jolt_finder(cache_dict, full_array, index+2)
    if index+3 < len(full_array) and full_array[index+3] - current_jolt <= 3:
        next_jolt3 = recursive_jolt_finder(cache_dict, full_array, index+3)

    cache_dict[str(index)] = next_jolt1 + next_jolt2 + next_jolt3
    return next_jolt1 + next_jolt2 + next_jolt3

