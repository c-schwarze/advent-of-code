import re

import helpers


RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def run():
    with open("year2023/day2/input.txt", "r") as f:
        full_string = f.read()

    lines = []
    for x in full_string.splitlines():
        game_text, round_text = x.split(': ')
        lines.append({
            'game_num': int(game_text.split(' ')[1]),
            # TODO - consider expanding this to loop over each round
            'game': [round.split(', ') for round in round_text.split('; ')],
        })

    print("--- PART 1 ---")
    print("Sum all indexes of possible games: ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("Sum the power of all minimum needed cubes")
    print(part2(lines))


# answer = 2505
def part1(lines):

    total = 0
    for line in lines:
        game_num = line['game_num']
        game = line['game']
        is_valid = True
        for round in game:
            if not is_valid_round(round):
                is_valid = False
                break

        if is_valid:
            total += game_num

    return total


# answer = 70265
def part2(lines):

    total = 0
    for line in lines:
        game_num = line['game_num']
        game = line['game']

        current_max_red = 0
        current_max_green = 0
        current_max_blue = 0
        for round in game:
            for draw in round:
                num, color = draw.split(' ')
                if color == 'red' and int(num) > current_max_red:
                    current_max_red = int(num)
                elif color == 'green' and int(num) > current_max_green:
                    current_max_green = int(num)
                elif color == 'blue' and int(num) > current_max_blue:
                    current_max_blue = int(num)
        total += current_max_red * current_max_green * current_max_blue

    return total


def is_valid_round(round):
    for draw in round:
        num, color = draw.split(' ')
        if color == 'red' and int(num) <= RED_MAX:
            continue
        elif color == 'green' and int(num) <= GREEN_MAX:
            continue
        elif color == 'blue' and int(num) <= BLUE_MAX:
            continue
        else:
            return False

    return True