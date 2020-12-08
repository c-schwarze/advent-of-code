def day7():
    with open("year2020/day7/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print('Part 1 - Number of bags that can hold shiny gold:')
    print(part1(full_array))
    print('Part 2 - How many bags does the shiny gold bag hold?')
    print(part2(full_array))


# answer = 378
def part1(full_array):
    color_holder = {}
    for line in full_array:
        split_parts = line.split(' contain ')
        bag_holder = convert_to_key(split_parts[0])
        color_holder[bag_holder] = []
        for bag in split_parts[1].split(', '):
            bag_parts = bag.split(" ", 1)
            bag_type = bag_parts[1].strip('.')
            carry_bags = convert_to_key(bag_type)
            if carry_bags != 'other-bag':
                color_holder[bag_holder].append(carry_bags)

    count = 0
    for key, bags in color_holder.items():
        count += recurse_for_gold_shiny_bags(color_holder, key)

    return count


# answer = 27526
def part2(full_array):
    # loop over everything to count things
    color_holder = {}
    for line in full_array:
        split_parts = line.split(' contain ')
        bag_holder = convert_to_key(split_parts[0])
        color_holder[bag_holder] = []
        for bag in split_parts[1].split(', '):
            bag_parts = bag.split(" ", 1)
            num_bags= bag_parts[0]
            bag_type = bag_parts[1].strip('.')
            carry_bags = convert_to_key(bag_type)
            if carry_bags != 'other-bag':
                bag_dict = {
                    'num': int(num_bags),
                    'bag': carry_bags
                }
                color_holder[bag_holder].append(bag_dict)

    return recurse_count_bags(color_holder, 'shiny-gold-bag') - 1


def convert_to_key(string):
    new_key = string.replace(' ', '-')
    if new_key[-1] == 's':
        new_key = new_key[:-1]
    return new_key


def recurse_for_gold_shiny_bags(color_holder, key):
    bags = color_holder[key]
    for bag in bags:
        if bag == 'shiny-gold-bag' or bag == 'shiny-gold-bags':
            return 1
        else:
            find_gold_bags = recurse_for_gold_shiny_bags(color_holder, bag)
            if find_gold_bags:
                return find_gold_bags

    return 0


def recurse_count_bags(color_holder, bag):
    try:
        bags = color_holder[bag]
    except KeyError:
        return 1

    if len(bags) == 0:
        return 1

    count = 0
    for bag_dict in bags:
        for num in range(0, bag_dict['num']):
            count += recurse_count_bags(color_holder, bag_dict['bag'])
    return 1 + count
