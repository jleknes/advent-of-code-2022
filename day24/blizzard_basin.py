import fileinput, time

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

blizzard_directions = {"<": LEFT, ">": RIGHT, "^": UP, "v": DOWN}

blizzards = set()

blizzards_minutes = {}


def read_input():
    line_count = 0
    global length, width
    for line in fileinput.input():
        for i in range(1, len(line.strip()) - 1):
            if line[i] in blizzard_directions.keys():
                blizzards.add((line_count - 1, i - 1, blizzard_directions[line[i]]))
        line_count += 1
        width = len(line.strip()) - 2
    length = line_count - 2


def generate_grid():
    blizzards_minutes[0] = set()
    for blizzard in blizzards:
        blizzards_minutes[0].add((blizzard[0], blizzard[1]))
    for i in range(1, 1000):
        new_blizzards = set()
        for blizzard in blizzards:
            dx, dy = 0, 0
            if blizzard[2] == LEFT:
                dx = -i
            elif blizzard[2] == RIGHT:
                dx = i
            elif blizzard[2] == DOWN:
                dy = i
            else:
                dy = -i

            y = (blizzard[0] + dy) % length
            x = (blizzard[1] + dx) % width
            # print(blizzard, "dy,dx:", dy, dx, "y,x", y, x)
            new_blizzards.add((y, x))
        blizzards_minutes[i] = new_blizzards


def get_candiates(y, x, minutes):
    dy_dx = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
    adj = []
    for change in dy_dx:
        candidate_position = (y + change[0], x + change[1])
        start_pos = candidate_position[0] == -1 and candidate_position[1] == 0
        end_pos = candidate_position[0] == length and candidate_position[1] == width - 1
        in_grid = (
            candidate_position[0] >= 0
            and candidate_position[0] < length
            and candidate_position[1] >= 0
            and candidate_position[1] < width
        )
        if (in_grid or start_pos or end_pos) and candidate_position not in blizzards_minutes[minutes]:
            adj.append(candidate_position)
    return adj


def solve(position, goal, minutes_passed):
    y, x = position[0], position[1]
    goal_y, goal_x = goal[0], goal[1]
    visited = []  # List for visited nodes.
    queue = []
    # visited.append((y, x, minutes_passed))
    queue.append((y, x))

    while len(queue) > 0:
        level_size = len(queue)
        # print(queue)
        while level_size > 0:
            position = queue.pop(0)
            # print(position)
            if position[0] == goal_y and position[1] == goal_x:
                return minutes_passed
            for candidate_position in get_candiates(position[0], position[1], minutes_passed):
                # print("candidate:", candidate_position)
                if candidate_position not in queue:
                    # print("candidate:", candidate_position)
                    queue.append(candidate_position)
            level_size -= 1
        minutes_passed += 1


def print_grid():
    for i in range(20):
        print(f"round {i}")
        for y in range(length):
            line = "#"
            for x in range(width):
                if (y, x) in blizzards_minutes[i]:
                    line += "x"
                else:
                    line += " "
            line += "#"
            print(line)


read_input()
generate_grid()
# print(blizzards_minutes)
start_time = time.time()
to_goal = solve((-1, 0), (length - 1, width - 1), 0)
print("part one:", to_goal)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
back_again = solve((length, width - 1), (-1, 0), to_goal)
part_two = solve((-1, 0), (length - 1, width - 1), back_again)
print("part two:", part_two)
print("--- %s seconds ---" % (time.time() - start_time))

# print_grid()
