import re


def day4():
    with open("year2020/day4/input.txt", "r") as f:
        full_string = f.read()

    full_array = split_on_empty_lines(full_string)

    print(part1(full_array))
    print(part2(full_array))


# answer = 202
def part1(full_array):
    count = 0
    for line in full_array:
        if is_valid_passport(line.replace('\n', ' ').replace('\r', '').split(' ')):
            count += 1
    return count


# answer = 137
def part2(full_array):
    count = 0
    for line in full_array:
        if is_valid_passport_validation(line.replace('\n', ' ').replace('\r', '').split(' ')):
            count += 1
    return count


def is_valid_passport(array_of_key_values):
    checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for check in checks:
        found_check = False
        for key_value in array_of_key_values:
            key_value_array = key_value.split(':')
            if key_value_array[0] == check:
                found_check = True

        if not found_check:
            return False
    return True


def is_valid_passport_validation(array_of_key_values):
    checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for check in checks:
        pass_check = False
        for key_value in array_of_key_values:
            key_value_array = key_value.split(':')
            if key_value_array[0] == check:
                # good
                if check == 'byr':
                    try:
                        int(key_value_array[1])
                    except:
                        continue
                    if len(key_value_array[1]) == 4 and int(key_value_array[1]) >= 1920 and int(key_value_array[1]) <= 2002:
                        pass_check = True
                # good
                if check == 'iyr':
                    try:
                        int(key_value_array[1])
                    except:
                        continue
                    if len(key_value_array[1]) == 4 and int(key_value_array[1]) >= 2010 and int(key_value_array[1]) <= 2020:
                        pass_check = True
                # good
                if check == 'eyr':
                    try:
                        int(key_value_array[1])
                    except:
                        continue
                    if len(key_value_array[1]) == 4 and int(key_value_array[1]) >= 2020 and int(key_value_array[1]) <= 2030:
                        pass_check = True
                # good
                if check == 'hgt':
                    if 'cm' in key_value_array[1]:
                        the_num = key_value_array[1].replace('cm', '')
                        if int(the_num) >= 150 and int(the_num) <= 193:
                            pass_check = True
                    if 'in' in key_value_array[1]:
                        the_num = key_value_array[1].replace('in', '')
                        if int(the_num) >= 59 and int(the_num) <= 76:
                            pass_check = True
                # good
                if check == 'hcl':
                    regex = r"#[0-9a-f]"
                    if re.split(regex, key_value_array[1]) and len(key_value_array[1])==7:
                        pass_check = True
                # good
                if check == 'ecl':
                    for eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        if key_value_array[1] == eye_color:
                            pass_check = True
                # good
                if check == 'pid':
                    try:
                        int(key_value_array[1])
                    except:
                        pass
                    if len(key_value_array[1]) == 9 and re.split(r"[0-9]*", key_value_array[1]):
                        pass_check = True

        if not pass_check:
            return False
    return True


def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())