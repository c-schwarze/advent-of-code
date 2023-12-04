import re

import helpers


def run():
    with open("year2023/day1/input.txt", "r") as f:
        full_string = f.read()

    lines = []
    for x in full_string.splitlines():
        lines.append(x.split(' '))

    print("--- PART 1 ---")
    print("Sum of all calibration values: ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("Also read numbers by strings")
    print(part2(lines))


# answer = 54697
def part1(lines):

    total = 0
    for line in lines:
        line_string = str(line)
        try:
            new_num = int(re.search(r'\d+', line_string).group()[0] + re.search(r'\d+', line_string[::-1]).group()[0])
            total += new_num
        except:
            continue

    return total


# answer = 54885
def part2(lines):
    # we are going to do a greedy approach.

    total = 0
    for line in lines:
        line_string = str(line)
        first_num = convertTextToNum(re.search(r'(\d+|one|two|three|four|five|six|seven|eight|nine)', line_string).group(), False)
        second_num = convertTextToNum(re.search(r'(\d+|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)', line_string[::-1]).group(), True)
        total += int(first_num+second_num)

    return total


def convertTextToNum(string, reverse_if_not_num: bool):
    converted_string = string
    if reverse_if_not_num:
        try:
            int(converted_string)
        # todo - I should be adding a specific exception
        except:
            converted_string = converted_string[::-1]

    if converted_string == 'one':
        return '1'
    elif converted_string == 'two':
        return '2'
    elif converted_string == 'three':
        return '3'
    elif converted_string == 'four':
        return '4'
    elif converted_string == 'five':
        return '5'
    elif converted_string == 'six':
        return '6'
    elif converted_string == 'seven':
        return '7'
    elif converted_string == 'eight':
        return '8'
    elif converted_string == 'nine':
        return '9'
    else:
        return converted_string[0]
