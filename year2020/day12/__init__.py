def day12():
    with open("year2020/day12/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print('Part 1 - Manhattan distance to ending point')
    print(part1(full_array))
    print('Part 2 - Same, but using waypoint')
    print(part2(full_array))


# answer = 415
def part1(full_array):
    facing = 0  # east
    current_x = 0
    current_y = 0
    for action in full_array:
        distance = int(action[1:])
        if 'N' in action:
            current_y += distance
        elif 'S' in action:
            current_y -= distance
        elif 'E' in action:
            current_x += distance
        elif 'W' in action:
            current_x -= distance
        elif 'L' in action:
            facing = (facing - distance)%360
        elif 'R' in action:
            facing = (facing + distance)%360
        elif 'F' in action:
            if facing == 0:
                current_x += distance
            elif facing == 90:
                current_y -= distance
            elif facing == 180:
                current_x -= distance
            elif facing == 270:
                current_y += distance

    return manhattan_distance(current_x, current_y)


# answer = 29401
def part2(full_array):
    current_x = 0
    current_y = 0
    waypoint_x = 10
    waypoint_y = 1

    for action in full_array:
        distance = int(action[1:])
        print(action)
        if 'N' in action:
            waypoint_y += distance
        elif 'S' in action:
            waypoint_y -= distance
        elif 'E' in action:
            waypoint_x += distance
        elif 'W' in action:
            waypoint_x -= distance
        elif 'L' in action:
            old_waypoint_x = waypoint_x
            old_waypoint_y = waypoint_y

            if distance == 0:
                continue
            elif distance == 90:
                waypoint_x = -old_waypoint_y
                waypoint_y = old_waypoint_x
            elif distance == 180:
                waypoint_x = -old_waypoint_x
                waypoint_y = -old_waypoint_y
            elif distance == 270:
                waypoint_x = old_waypoint_y
                waypoint_y = -old_waypoint_x

        elif 'R' in action:
            old_waypoint_x = waypoint_x
            old_waypoint_y = waypoint_y

            if distance == 0:
                continue
            elif distance == 90:
                waypoint_x = old_waypoint_y
                waypoint_y = -old_waypoint_x
            elif distance == 180:
                waypoint_x = -old_waypoint_x
                waypoint_y = -old_waypoint_y
            elif distance == 270:
                waypoint_x = -old_waypoint_y
                waypoint_y = old_waypoint_x
        elif 'F' in action:
            current_x += waypoint_x * distance
            current_y += waypoint_y * distance

        print('ship position', current_x, current_y)
        print('waypoint', waypoint_x, waypoint_y)

    return manhattan_distance(current_x, current_y)


def manhattan_distance(x, y):
    return abs(x) + abs(y)