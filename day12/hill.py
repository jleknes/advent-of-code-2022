import fileinput, queue


def getOptions(grid, visited, point):
    curr = grid[point[0]][point[1]]
    points = []
    newpoints = [(point[0] - 1, point[1]), (point[0], point[1] - 1), (point[0] + 1, point[1]), (point[0], point[1] + 1)]
    for newpoint in newpoints:
        if newpoint[0] >= 0 and newpoint[0] < len(grid) and newpoint[1] >= 0 and newpoint[1] < len(grid[newpoint[0]]):
            if newpoint not in visited and grid[newpoint[0]][newpoint[1]] <= curr + 1:
                points.append(newpoint)
    return points


def solve(start, end, grid):
    count = -1
    visited = set()
    next = set()
    next.add(start)
    while count < 1000:
        count += 1
        next_2 = set()
        while len(next) > 0:
            point = next.pop()
            visited.add(point)
            if point == end:
                return count

            next_points = getOptions(grid, visited, point)
            for option in next_points:
                next_2.add(option)
        next = next_2
    return 10000


def read_input():
    grid = []
    start = (0, 0)
    end = (0, 0)
    y = 0
    for line in fileinput.input():
        gridline = []
        for x in range(len(line.strip())):
            if line[x] == "S":
                gridline.append(ord("z"))
                start = (y, x)
            elif line[x] == "E":
                gridline.append(ord("z"))
                end = (y, x)
            else:
                gridline.append(ord(line[x]))
        grid.append(gridline)
        y += 1
    return start, end, grid


def part_one():
    start, end, grid = read_input()
    count = solve(start, end, grid)
    print("part one", count)


def part_two():
    start, end, grid = read_input()
    min_length = 10000
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ord("a"):
                length = solve((y, x), end, grid)
                if length < min_length:
                    min_length = length

    print("part two", min_length)


# part_one()

part_two()
