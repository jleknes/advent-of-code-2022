import fileinput

visited = set()


def tail_position(headx, heady, tailx, taily):
    print("before move of tail ", "head:", headx, ",", heady, "tail:", tailx, ",", taily)

    global visited
    dx = headx - tailx
    dy = heady - taily
    if abs(dx) < 2 and abs(dy) < 2:
        return (tailx, taily)
    # diagonal move
    elif abs(dx) + abs(dy) == 3:
        if abs(dx) == 2:
            tailx += int(dx / 2)
            taily += dy
        else:
            tailx += dx
            taily += int(dy / 2)
    else:
        if abs(dx) == 2:
            tailx += int(dx / 2)
        else:
            taily += int(dy / 2)
    visited.add((tailx, taily))
    print("Tail moved to:", "tail:", tailx, ",", taily)
    return (tailx, taily)


def main():
    global visited
    headx, heady, tailx, taily = 0, 0, 0, 0
    visited.add((tailx, taily))
    for line in fileinput.input():
        direction, steps = line.split()[0], int(line.split()[1])
        match direction:
            case "R":
                for i in range(steps):
                    headx += 1
                    tailx, taily = tail_position(headx, heady, tailx, taily)
            case "U":
                for i in range(steps):
                    heady -= 1
                    tailx, taily = tail_position(headx, heady, tailx, taily)
            case "D":
                for i in range(steps):
                    heady += 1
                    tailx, taily = tail_position(headx, heady, tailx, taily)
            case "L":
                for i in range(steps):
                    headx -= 1
                    tailx, taily = tail_position(headx, heady, tailx, taily)
    print(len(visited))


def move(positions, movex, movey):
    global visited
    positions[0] = Point(positions[0].x + movex, positions[0].y + movey)
    for i in range(1, len(positions)):
        dx = positions[i - 1].x - positions[i].x
        dy = positions[i - 1].y - positions[i].y
        # diagonal move
        if abs(dx) + abs(dy) == 4:
            positions[i] = Point(positions[i].x + int(dx / 2), positions[i].y + int(dy / 2))
        elif abs(dx) + abs(dy) == 3:
            if abs(dx) == 2:
                positions[i] = Point(positions[i].x + int(dx / 2), positions[i].y + dy)
            else:
                positions[i] = Point(positions[i].x + dx, positions[i].y + int(dy / 2))
        elif abs(dx) == 2 and abs(dy) == 0:
            positions[i] = Point(positions[i].x + int(dx / 2), positions[i].y)
        elif abs(dy) == 2 and abs(dx) == 0:
            positions[i] = Point(positions[i].x + dx, positions[i].y + int(dy / 2))
        print("positions[", i, "]", positions[i], "dx", dx, "dy", dy)
    visited.add(positions[9])
    return positions


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


def part_two():
    global visited
    positions = []
    for i in range(0, 10):
        positions.append(Point(0, 0))
    for line in fileinput.input():
        direction, steps = line.split()[0], int(line.split()[1])
        match direction:
            case "R":
                for i in range(steps):
                    positions = move(positions, 1, 0)
            case "U":
                for i in range(steps):
                    positions = move(positions, 0, -1)
            case "D":
                for i in range(steps):
                    positions = move(positions, 0, 1)
            case "L":
                for i in range(steps):
                    positions = move(positions, -1, 0)
    for point in visited:
        print(point)
    print(len(visited))


part_two()
