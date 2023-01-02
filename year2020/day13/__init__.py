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
    bus_schedule = full_array[1].split(',')

    buses = []
    mod_num = len(bus_schedule)

    the_mod_numbers = []
    the_timestamps = bus_schedule
    chinese_remainder(the_mod_numbers, the_timestamps)


    multiplier = 100000000000000/int(bus_schedule[0])
    earliest_timestamp = 0
    iterated_every_num = False
    while not iterated_every_num:
        get_me_out = False
        multiplier += 1
        print(multiplier)
        for index, bus in enumerate(bus_schedule):
            if bus == 'x':
                continue

            int_bus = int(bus)
            if index == 0:
                earliest_timestamp = int_bus * multiplier
                continue

            bus_check = 100000000000000
            while bus_check <= earliest_timestamp:
                bus_check += int_bus

            if earliest_timestamp + index != bus_check:
                get_me_out = True
                break
        if get_me_out:
            continue
        iterated_every_num = True

    return earliest_timestamp

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


from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1