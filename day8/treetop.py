import fileinput


def count(grid, x, y, dx, dy):
    global visible
    max_height = grid[x][y]
    x += dx
    y += dy
    while x > 0 and x < len(grid) - 1 and y > 0 and y < len(grid) - 1:
        if grid[x][y] > max_height:
            max_height = grid[x][y]
            visible[x][y] = True
        # cutoff
        if max_height == 9:
            return
        x += dx
        y += dy


def count_trees(grid, x, y, dx, dy):
    height = grid[x][y]
    x += dx
    y += dy
    count = 0
    while x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
        if grid[x][y] < height:
            count += 1
        elif grid[x][y] >= height:
            count += 1
            return count
        x += dx
        y += dy
    return count


def scenic_score(grid, x, y):
    score = 1
    # to the north
    score *= count_trees(grid, x, y, 0, -1)
    # to the east
    score *= count_trees(grid, x, y, 1, 0)
    # to the south
    score *= count_trees(grid, x, y, 0, 1)
    # to the west
    score *= count_trees(grid, x, y, -1, 0)
    return score


def read_input():
    grid = []
    pos = 0
    for line in fileinput.input():
        grid.append([])
        for i in range(0, len(line.strip())):
            grid[pos].append(int(line[i]))
        pos += 1
    return grid


def solve():
    grid = read_input()
    global visible
    visible = [[False for j in range(len(grid))] for i in range(len(grid))]

    # from north
    for i in range(1, len(grid) - 1):
        count(grid, i, 0, 0, 1)
    # from east
    for i in range(1, len(grid) - 1):
        count(grid, len(grid) - 1, i, -1, 0)
    # from south
    for i in range(1, len(grid) - 1):
        count(grid, i, len(grid) - 1, 0, -1)
    # from west
    for i in range(1, len(grid) - 1):
        count(grid, 0, i, 1, 0)
    sum = 0
    for i in range(0, len(visible)):
        for j in range(0, len(visible)):
            if visible[i][j]:
                sum += 1
    sum += 4 * len(visible) - 4
    print("part one:", sum)
    max_scenic_score = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            score = scenic_score(grid, i, j)
            if score > max_scenic_score:
                max_scenic_score = score
    print("part two:", max_scenic_score)


solve()
