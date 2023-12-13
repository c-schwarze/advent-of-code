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
    assert part1(lines) == 35
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
                almanac[map_from]['lines'].append(line.split(' '))

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

    # This should build out our process
    for line in lines:
        if len(line) != 0:
            if line[0].isalpha():
                if 'seeds: ' in line:
                    almanac['seeds'] = []
                    # use [::2]
                    range_start = line.split(': ')[1].split(' ')[::2]
                    range_end = line.split(': ')[1].split(' ')[1::2]
                    for index in range(len(range_start)):
                        almanac['seeds'].append({
                            'range-start': range_start[index],
                            'range-end': range_end[index],
                        })
                else:
                    map_from = line.split('-to-')[0]
                    map_to = line.split('-to-')[1].replace(' map:', '')
                    almanac[map_from] = {
                        'from': map_from,
                        'to': map_to,
                        'ranges': []
                    }
            else:
                # TODO - this needs the values set properly
                almanac[map_from]['ranges'].append(line.split(' '))

    # TODO - work backwards, since we have a "limited" data set at the end
    lowest_seed_value = 1
    for lowest_seed_value in range(1,100000):

        from_directory = 'location'
        start_value = lowest_seed_value

        while from_directory != 'location':
            directory = almanac[from_directory]
            destination = directory['to']

            for specified_range in directory['lines']:
                if int(specified_range[1]) <= start_value <= int(specified_range[1]) + int(specified_range[2]):
                    start_value = start_value - int(specified_range[1]) + int(specified_range[0])
                    break

            # at the end, move on!
            from_directory = destination

    return lowest_seed_value
