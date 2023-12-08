import helpers

import math


def run():
    with open("year2023/day4/input.txt", "r") as f:
        full_string = f.read()

    games = []
    for x in full_string.splitlines():
        card_text, num_text = x.split(': ')
        winning_nums = []
        for num in num_text.split(' | ')[0].strip().split(' '):
            if num.strip() != '':
                winning_nums.append(num.strip())

        playing_nums = []
        for num in num_text.split(' | ')[1].strip().split(' '):
            if num.strip() != '':
                playing_nums.append(num.strip())

        games.append({
            'card_num': int(card_text.rsplit(' ', 1)[1]),
            # TODO - consider expanding this to loop over each round
            'winning_nums': winning_nums,
            'playing_nums': playing_nums,
        })

    print("--- PART 1 ---")
    print("Total Points ")
    print(part1(games))
    assert part1(games) == 20107
    print("--- PART 2 ---")
    print("Total Scratchcards")
    print(part2(games))
    assert part2(games) == 8172507


def part1(games):
    total_points = 0
    for game in games:
        winning_nums_found = 0
        for num in game['playing_nums']:
            if num in game['winning_nums']:
                winning_nums_found += 1

        # scoring
        total_points += int(math.pow(2, winning_nums_found - 1))

    return total_points


def part2(games):
    num_scratchcards = {}
    running_total = 0

    for game in games:
        num_scratchcards[game['card_num']] = 1

    for game in games:
        winning_nums_found = 0
        for num in game['playing_nums']:
            if num in game['winning_nums']:
                winning_nums_found += 1

        # scoring
        for copy in range(int(winning_nums_found)):
            try:
                num_scratchcards[game['card_num'] + 1 + copy ] += num_scratchcards[game['card_num']]
            except:
                pass

    for _, scratchcard in enumerate(num_scratchcards):
        running_total += num_scratchcards[scratchcard]

    return running_total
