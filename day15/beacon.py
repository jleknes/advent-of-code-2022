import fileinput, re, time

GRID_SIZE = 4000000


def readinput():
    sensors = []
    beacons = []
    for line in fileinput.input():
        match = re.findall(r"x=(-?\d+), y=(-?\d+)", line.strip())
        sensors.append(tuple(map(int, (match[0]))))
        beacons.append(tuple(map(int, (match[1]))))
    return sensors, beacons


def distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


def solve_part_one(sensors, beacons):
    x_points = set()
    y = 2000000
    for sensor, beacon in zip(sensors, beacons):
        beacon_dist = distance(sensor, beacon)
        y_dist = abs(sensor[1] - y)
        x_points_to_cover = beacon_dist - y_dist
        if x_points_to_cover > 0:
            for x in range(
                sensor[0] - x_points_to_cover,
                sensor[0] + x_points_to_cover,
            ):
                x_points.add(x)

    print("part one:", len(x_points))


def covers_x(sensor, beacon, y):
    beacon_dist = distance(sensor, beacon)
    y_dist = abs(sensor[1] - y)
    x_points_to_cover = beacon_dist - y_dist
    if x_points_to_cover > 0:
        x1 = sensor[0] - x_points_to_cover
        x2 = sensor[0] + x_points_to_cover
        if x1 < 0:
            x1 = 0
        if x2 > GRID_SIZE:
            x2 = GRID_SIZE
        return x1, x2
    else:
        return 0, 0


def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1] + 1:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


def solve_part_two(sensors, beacons):
    start_time = time.time()
    for y in range(0, GRID_SIZE):
        # y = 100
        intervals = []
        for sensor, beacon in zip(sensors, beacons):
            x1, x2 = covers_x(sensor, beacon, y)
            if not (x1 == 0 and x2 == 0):
                intervals.append([x1, x2])
        # print(intervals)
        if len(intervals) > 0:
            mergedIntervals = merge(intervals)
            if len(mergedIntervals) > 1:
                x = mergedIntervals[0][1] + 1
                print("part two:", x * 4000000 + y)
    print("--- %s seconds ---" % (time.time() - start_time))


sensors, beacons = readinput()
solve_part_one(sensors, beacons)
solve_part_two(sensors, beacons)
