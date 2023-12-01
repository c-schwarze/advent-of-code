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
    print("TODO: ")
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


# answer =
def part2(lines):
    # we are going to do a greedy approach.

    total = 0
    for line in lines:
        line_string = str(line)
        try:
            first_num = convertTextToNum(re.search(r'(\d+|one|two|three|four|five|six|seven|eight|nine)', line_string).group())
            # TODO - this one is the problem
            second_num = convertTextToNum(re.search(r'(\d+|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)', line_string[::-1]).group())
            total += int(first_num+second_num)
        except:
            continue

    return total


def convertTextToNum(string):
    if string == 'one':
        return '1'
    elif string == 'two':
        return '2'
    elif string == 'three':
        return '3'
    elif string == 'four':
        return '4'
    elif string == 'five':
        return '5'
    elif string == 'six':
        return '6'
    elif string == 'seven':
        return '7'
    elif string == 'eight':
        return '8'
    elif string == 'nine':
        return '9'
    else:
        return string[0]
