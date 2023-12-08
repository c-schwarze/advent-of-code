import helpers

import math


def run():
    with open("year2023/day5/input.txt", "r") as f:
        full_string = f.read()

    lines = []
    for x in full_string.splitlines():
        lines.append(x.strip())

    print("--- PART 1 ---")
    print("Lowest location num ")
    print(part1(lines))
    assert part1(lines) == 525792406
    print("--- PART 2 ---")
    print("")
    print(part2(lines))
    assert part2(lines) == 525792406


def part1(lines):
    almanac = {}
    map_from = ''
    for line in lines:
        if len(line) != 0:
            if line[0].isalpha():
                if 'seeds: ' in line:
                    almanac['seeds'] = line.split(': ')[1].split(' ')
                else:
                    map_from = line.split('-to-')[0]
                    map_to = line.split('-to-')[1].replace(' map:', '')
                    almanac[map_from] = {
                        'from': map_from,
                        'to': map_to,
                        'values': {},
                        'lines': [],
                    }
            else:
                almanac[map_from]['lines'].append(x.split(' '))

    lowest_seed_value = -1
    for seed in almanac['seeds']:
        from_directory = 'seed'
        start_value = int(seed)

        while from_directory != 'location':
            directory = almanac[from_directory]
            destination = directory['to']

            for specified_range in directory['lines']:
                if int(specified_range[1]) <= start_value <= int(specified_range[1]) + int(specified_range[2]):
                    start_value = start_value - int(specified_range[1]) + int(specified_range[0])
                    break

            # at the end, move on!
            from_directory = destination

        if lowest_seed_value == -1 or start_value <= lowest_seed_value:
            lowest_seed_value = start_value

    return lowest_seed_value


def part2(lines):
    almanac = {}
    map_from = ''
    for line in lines:
        if len(line) != 0:
            if line[0].isalpha():
                if 'seeds: ' in line:
                    almanac['seeds'] = line.split(': ')[1].split(' ')
                else:
                    map_from = line.split('-to-')[0]
                    map_to = line.split('-to-')[1].replace(' map:', '')
                    almanac[map_from] = {
                        'from': map_from,
                        'to': map_to,
                        'values': {},
                        'lines': [],
                    }
            else:
                almanac[map_from]['lines'].append(x.split(' '))

    lowest_seed_value = -1

    for index, seed_range in enumerate(almanac['seeds'][::2]):
        start = int(seed_range)
        end = int(seed_range) + int(almanac['seeds'][(index*2)+1])

        # todo - from here we need to connect the ranges together.
        #      - Range1 -> range2, but also due to overlap, Range1 -> range2b, etc.
        #      - With that mapping, then we need to find the lowest range.


        # TODO - a 2nd idea would be to try to work backwards, since we have a "limited" data set at the end


    return lowest_seed_value
