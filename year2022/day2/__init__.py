import helpers

# A/X - Rock
# B/Y - Paper
# C/Z - Scissors
def day2():
    f = open("year2022/day2/input.txt", "r")
    cheat_sheet = []
    for x in f:
        cheat_sheet.append(x.split(' '))

    print("--- PART 1 ---")
    print("Total Score: ")
    print(part1(cheat_sheet))
    print("--- PART 2 ---")
    print("Total Score: ")
    print(part2(cheat_sheet))


# answer = 11767
def part1(cheat_sheet):

    highest_total = 0
    for line in cheat_sheet:
        opponent = line[0]
        me = line[1].strip('\n')

        highest_total += score(opponent, me)

    return highest_total


# answer = 13886
def part2(cheat_sheet):

    highest_total = 0
    for line in cheat_sheet:
        opponent = line[0]
        desired_result = line[1].strip('\n')

        if desired_result == 'X':
            if opponent == 'A':
                me = 'Z'
            elif opponent == 'B':
                me = 'X'
            elif opponent == 'C':
                me = 'Y'
        elif desired_result == 'Y':
            if opponent == 'A':
                me = 'X'
            elif opponent == 'B':
                me = 'Y'
            elif opponent == 'C':
                me = 'Z'
        elif desired_result == 'Z':
            if opponent == 'A':
                me = 'Y'
            elif opponent == 'B':
                me = 'Z'
            elif opponent == 'C':
                me = 'X'

        highest_total += score(opponent, me)

    return highest_total


def score(opponent, me):
    score = 0

    # what you played scoring
    if readible_input(me) == 'Rock':
        score += 1
    elif readible_input(me) == 'Paper':
        score += 2
    elif readible_input(me) == 'Scissors':
        score += 3

    # result scoring
    if readible_input(opponent) == readible_input(me):
        score += 3
    elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
        score += 6

    return score


def readible_input(input):
    if input == 'A' or input == 'X':
        return 'Rock'
    if input == 'B' or input == 'Y':
        return 'Paper'
    if input == 'C' or input == 'Z':
        return 'Scissors'