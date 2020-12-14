def day13():
    with open("year2020/day13/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print('Part 1 - ')
    print(part1(full_array))
    print('Part 2 - ')
    print(part2(full_array))


# answer = 6568
def part1(full_array):
    seconds = int(full_array[0])
    bus_schedule = full_array[1].split(',')

    buses = []
    for bus in bus_schedule:
        if bus == 'x':
            continue

        # loop over
        bus_loop = int(bus)
        while bus_loop < seconds:
            bus_loop += int(bus)

        buses.append({
            'id': int(bus),
            'num': bus_loop,
            'difference': bus_loop - seconds
        })

    buses = sorted(buses, key = lambda i: i['difference'])
    return buses[0]['id'] * buses[0]['difference']


def part2(full_array):
    
    return 'todo: figure out how to do chinese remainder theorom with this...'

# answer = ?? This works, but it takes FOREVER
# def part2_v1(full_array):
#     bus_schedule = full_array[1].split(',')
#
#     buses = []
#     mod_num = len(bus_schedule)
#     multiplier = 100000000000000/int(bus_schedule[0])
#     earliest_timestamp = 0
#     iterated_every_num = False
#     while not iterated_every_num:
#         get_me_out = False
#         multiplier += 1
#         print(multiplier)
#         for index, bus in enumerate(bus_schedule):
#             if bus == 'x':
#                 continue
#
#             int_bus = int(bus)
#             if index == 0:
#                 earliest_timestamp = int_bus * multiplier
#                 continue
#
#             bus_check = 100000000000000
#             while bus_check <= earliest_timestamp:
#                 bus_check += int_bus
#
#             if earliest_timestamp + index != bus_check:
#                 get_me_out = True
#                 break
#         if get_me_out:
#             continue
#         iterated_every_num = True
#
#     return earliest_timestamp
