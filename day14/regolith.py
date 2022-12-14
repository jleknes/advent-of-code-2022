import fileinput, time

line_pos = set()
segments = []
max_y = 0


def blocked(x, y, sand_pos):
    if (x, y) in sand_pos or (x, y) in line_pos:
        return True
    return False


def unit_of_sand(sand_pos):
    xpos = 500
    ypos = 0
    rest = False
    while rest == False and ypos < max_y + 2:
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
    return rest


def simulate_sand():
    sand_pos = set()
    rest = True
    while rest:
        rest = unit_of_sand(sand_pos)
    return len(sand_pos)


def simulate_sand_2():
    sand_pos = set()

    while not (500, 0) in sand_pos:
        unit_of_sand(sand_pos)

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
    start_time = time.time()
    print("part one:", simulate_sand())
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    for x in range(500 - max_y - 10, 500 + max_y + 10):
        line_pos.add((x, max_y + 2))
    print("part two:", simulate_sand_2())
    print("--- %s seconds ---" % (time.time() - start_time))


solve()
