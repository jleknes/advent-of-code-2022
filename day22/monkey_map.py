import fileinput, time, re

grid = []


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
# (y,x)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
commands = []


def read_input():
    # find longe
    lines = []
    for line in fileinput.input():
        lines.append(line)
    grid_width = len(max(lines[0 : len(lines) - 2], key=len))
    print(grid_width)
    for line in lines:
        if "." in line or "#" in line:
            grid.append(line[0 : len(line) - 1].ljust(grid_width - 1))
        elif len(line) > 1:
            commands.extend(re.findall(r"\d+|\D", line.strip()))
    print(commands)
    for line in grid:
        print(line.replace(" ", "_"))


def turn(current, direction):
    if direction == "L":
        return (current - 1) % 4
    else:
        return (current + 1) % 4


def simulate():
    width = len(grid[0])
    height = len(grid)
    pos = (0, grid[0].index("."))
    print("height, width:", height, width)
    print(commands)
    print(pos)
    direction = RIGHT
    for command in commands:
        print("command:", command)
        if command.isnumeric():
            for i in range(int(command)):
                next_y, next_x = pos[0] + directions[direction][0], pos[1] + directions[direction][1]
                if next_y == height:
                    next_y = 0
                if next_x == width:
                    next_x = 0
                if next_x == -1:
                    next_x = width - 1
                if next_y == -1:
                    next_y = height - 1
                if grid[next_y][next_x] == " ":
                    if direction == LEFT or direction == RIGHT:
                        width_of_line = width - grid[next_y].count(" ")
                        leading_spaces = len(grid[next_y]) - len(grid[next_y].lstrip())
                        if direction == LEFT:
                            next_x = leading_spaces + width_of_line - 1
                        else:
                            next_x = leading_spaces
                    else:
                        if direction == DOWN:
                            i = 0
                            while grid[i][next_x] == " ":
                                i += 1
                            next_y = i
                        else:
                            i = height - 1
                            while grid[i][next_x] == " ":
                                i -= 1
                            next_y = i

                if grid[next_y][next_x] == "#":
                    print(i, "ran into wall")
                    break
                else:
                    pos = (next_y, next_x)
                    print("updated position, new position:", pos)
        else:
            direction = turn(direction, command)
        print(pos, direction)
    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction)


def simulate_part_two():
    width = len(grid[0])
    height = len(grid)
    pos = (0, grid[0].index("."))
    print("height, width:", height, width)
    print(commands)
    print(pos)
    direction = RIGHT
    for command in commands:
        print("command:", command)
        if command.isnumeric():
            for i in range(int(command)):
                next_y, next_x = pos[0] + directions[direction][0], pos[1] + directions[direction][1]
                # Det enkleste er å behandle hver kant individuelt. totalt 2*3+4*2=10 posisjoner som må hånteres
                # if x==width: fra side 1 til side 4
                # if y<0 and x>99: fra side 1 til side 5
                # if y<0 and x<100: fra side 2 til side 6
                # if x<0: and 99<y<150: til venstre for side 5
                # if x<50: y<50: til venstre for side 2, skal kobles til side 5
                # if x<0...

                if grid[next_y][next_x] == " ":
                    if direction == LEFT or direction == RIGHT:
                        width_of_line = width - grid[next_y].count(" ")
                        leading_spaces = len(grid[next_y]) - len(grid[next_y].lstrip())
                        if direction == LEFT:
                            next_x = leading_spaces + width_of_line - 1
                        else:
                            next_x = leading_spaces
                    else:
                        if direction == DOWN:
                            i = 0
                            while grid[i][next_x] == " ":
                                i += 1
                            next_y = i
                        else:
                            i = height - 1
                            while grid[i][next_x] == " ":
                                i -= 1
                            next_y = i

                if grid[next_y][next_x] == "#":
                    print(i, "ran into wall")
                    break
                else:
                    pos = (next_y, next_x)
                    print("updated position, new position:", pos)
        else:
            direction = turn(direction, command)
        print(pos, direction)
    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction)


read_input()
simulate()
