import copy


def day5():
    f = open("year2022/day5/input.txt", "r")
    lines = []
    for x in f:
        lines.append(x.strip('\n'))

    # build the arrays
    stacks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    turn_on_instructions = False
    instructions = []
    for line in lines:
        if turn_on_instructions:
            instructions.append(line)
        else:
            if line == '':
                turn_on_instructions = True
                continue
            if line.strip()[0] == '1':
                continue
            split_on_every_4th = [line[i:i + 4].strip() for i in range(0, len(line), 4)]
            print(split_on_every_4th)
            for index, item in enumerate(split_on_every_4th):
                if item != '':
                    stacks[index].insert(0, item.strip('[').strip(']'))

    print("--- PART 1 ---")
    print(part1(copy.deepcopy(stacks), instructions))
    print("--- PART 2 ---")
    print(part2(copy.deepcopy(stacks), instructions))


# answer = TLFGBZHCN
def part1(stacks, instructions):
    for instruction in instructions:
        num, from_stack, to_stack = instruction.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')

        for index in range(int(num)):
            stacks[int(to_stack)-1].append(stacks[int(from_stack) - 1].pop())

    return print_final_string(stacks)


# answer = QRQFHFWCL
def part2(stacks, instructions):
    for instruction in instructions:
        num, from_stack, to_stack = instruction.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')

        boxes_to_stack = []
        for index in range(int(num)):
            boxes_to_stack.append(stacks[int(from_stack) - 1].pop())
        boxes_to_stack.reverse()
        for box in boxes_to_stack:
            stacks[int(to_stack)-1].append(box)

    return print_final_string(stacks)


def print_final_string(stacks):
    final_string = ''
    for stack in stacks:
        if len(stack) > 0:
            final_string += stack[-1]
    return final_string
