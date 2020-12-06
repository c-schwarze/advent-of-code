def day2():
    with open("year2020/day2/input.txt", "r") as f:
        passwords = f.read().splitlines()

    print(part1(passwords))
    print(part2(passwords))


# answer = 660
def part1(passwords):
    total_valid_passwords = 0
    for x in passwords:
        pass_details = x.split(' ')

        pass_amounts = pass_details[0].split('-')
        pass_min = int(pass_amounts[0])
        pass_max = int(pass_amounts[1])

        pass_letter = pass_details[1][0]

        password = pass_details[2]
        pass_letter_count = password.count(pass_letter)
        if pass_max >= pass_letter_count and pass_letter_count >= pass_min:
            total_valid_passwords += 1

    return total_valid_passwords


# answer = 530
def part2(passwords):
    total_valid_passwords = 0
    for x in passwords:
        pass_details = x.split(' ')

        pass_amounts = pass_details[0].split('-')
        pass_min = int(pass_amounts[0])-1
        pass_max = int(pass_amounts[1])-1

        pass_letter = pass_details[1][0]

        password = pass_details[2]

        a = password[pass_min] == pass_letter
        b = password[pass_max] == pass_letter
        if (a and not b) or (not a and b):
            total_valid_passwords += 1

    return total_valid_passwords