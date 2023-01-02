def day3():
    f = open("year2022/day3/input.txt", "r")
    rucksacks = []
    for x in f:
        rucksacks.append(x.strip())

    print("--- PART 1 ---")
    print("Sum of Priorities: ")
    print(part1(rucksacks))
    print("--- PART 2 ---")
    print("Sum of Group Priorities: ")
    print(part2(rucksacks))


# answer = 7446
def part1(rucksacks):

    sum_priorities = 0
    for rucksack in rucksacks:
        sum_priorities += get_priority_for_rucksack(rucksack)

    return sum_priorities


# answer = 2646
def part2(rucksacks):

    sum_priorities = 0
    rucksack_group = []
    for rucksack in rucksacks:
        rucksack_group.append(rucksack)
        if len(rucksack_group) == 3:
            found_letter = ''
            for i in rucksack_group[0]:
                for j in rucksack_group[1]:
                    if i != j:
                        continue
                    for k in rucksack_group[2]:
                        if j != k:
                            continue
                        if i == j and j == k:
                            found_letter = i

            sum_priorities += get_priority(found_letter)
            rucksack_group = []

    return sum_priorities


def get_priority_for_rucksack(rucksack):
    line_divider = int(len(rucksack) / 2)
    first_compartment = rucksack[0:line_divider]
    second_compartment = rucksack[line_divider:]

    letter = compare_compartments(first_compartment, second_compartment)
    return get_priority(letter)

    print('{} {} | {} | {}'.format(first_compartment, second_compartment, letter, get_priority(letter)))

def compare_compartments(comp1, comp2):
    for i in comp1:
        for j in comp2:
            if i == j:
                return i
    return 'ERROR'


def get_priority(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96