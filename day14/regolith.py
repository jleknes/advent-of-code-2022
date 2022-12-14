import fileinput

line_pos = set()

segments = []

max_y = 0


def blocked(x, y, sand_pos):
    if (x, y) in sand_pos:
        return True

    if (x, y) in line_pos:
        return True

    return False


def blocked_2(x, y, sand_pos):
    if (x, y) in sand_pos:
        return True

    if (x, y) in line_pos:
        return True

    if y > max_y + 1:
        return True
    return False


def simulate_sand():
    sand_pos = set()
    ypos = 0
    while ypos < max_y + 2:
        xpos = 500
        ypos = 0
        rest = False
        while rest == False and ypos < 500:
            if not blocked(xpos, ypos + 1, sand_pos):
                ypos += 1
            else:
                if blocked(xpos - 1, ypos + 1, sand_pos):
                    if blocked(xpos + 1, ypos + 1, sand_pos):
                        rest = True
                    else:
                        ypos += 1
                        xpos += 1
                else:
                    ypos += 1
                    xpos -= 1

        if rest:
            sand_pos.add((xpos, ypos))

    return len(sand_pos)


def simulate_sand_2():
    sand_pos = set()

    while not (500, 0) in sand_pos:
        xpos = 500
        ypos = 0
        rest = False
        while rest == False:
            if not blocked_2(xpos, ypos + 1, sand_pos):
                ypos += 1
            else:
                if blocked_2(xpos - 1, ypos + 1, sand_pos):
                    if blocked_2(xpos + 1, ypos + 1, sand_pos):
                        rest = True
                    else:
                        ypos += 1
                        xpos += 1
                else:
                    ypos += 1
                    xpos -= 1

        if rest:
            sand_pos.add((xpos, ypos))

    return len(sand_pos)


def read_lines():
    global segments, max_y

    for line in fileinput.input():
        prev = (-1, -1)
        for point in line.strip().split(" -> "):
            x, y = list(map(int, point.split(",")))
            if y > max_y:
                max_y = y
            if prev != (-1, -1):
                for x1 in range(min(x, prev[0]), max(x, prev[0]) + 1):
                    for y1 in range(min(y, prev[1]), max(y, prev[1]) + 1):

                        line_pos.add((x1, y1))
                segments.append((prev, (x, y)))
            prev = (x, y)


def solve():
    read_lines()
    print("part one:", simulate_sand())

    print("part two:", simulate_sand_2())


solve()
