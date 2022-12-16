import fileinput, itertools
from functools import cache

flow_rate = {}
paths = {}
functioning_valves = []
simplified_paths = {}


def readinput():
    for line in fileinput.input():
        valve = line[6:8]
        rate = line[line.index("=") + 1 : line.index(";")]
        tunnels = [path.strip() for path in line[line.index("valve") + 6 :].strip().split(",")]
        print(valve, rate, tunnels)
        flow_rate[valve] = int(rate)
        paths[valve] = tunnels
        if flow_rate[valve] > 0:
            functioning_valves.append(valve)


visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def simplify_paths():
    for valve in functioning_valves + ["AA"]:
        # BFS to find shortest path between functioning valves
        queue = []
        visited = []
        queue.append(valve)
        visited.append(valve)
        len = 0
        while queue and len(simplified_paths[valve] < functioning_valves):
            next_valve = queue.pop(0)
            len += 1
            for path in paths[next_valve]:
                if not path in visited:
                    visited.append(path)
                    queue.append(path)
    print(simplified_paths)


readinput()
# simplify_paths()

print(flow_rate)
print(paths)
print(functioning_valves)

distances = {
    "AA": {"JJ": 2, "BB": 1, "DD": 1, "CC": 2, "EE": 3, "HH": 6},
    "BB": {"AA": 1, "JJ": 3, "DD": 2, "CC": 1, "EE": 2, "HH": 5},
    "CC": {"JJ": 4, "BB": 1, "DD": 1, "AA": 2, "EE": 1, "HH": 4},
    "DD": {"JJ": 3, "BB": 2, "CC": 1, "AA": 1, "EE": 1, "HH": 5},
    "EE": {"JJ": 5, "BB": 2, "DD": 2, "AA": 3, "CC": 1, "HH": 3},
    "HH": {"JJ": 8, "BB": 5, "DD": 5, "AA": 6, "EE": 3, "CC": 4},
    "JJ": {"CC": 4, "BB": 3, "DD": 3, "AA": 2, "EE": 5, "HH": 8},
}

# bitstring
def is_active(valve, code):
    # a bit expensive
    valvepos = functioning_valves.index(valve)
    return (code >> valvepos) & 1


def set_active(valve, code):
    # a bit expensive
    valvepos = functioning_valves.index(valve)
    return code | 1 << valvepos


# TODO: code active_valves as an int to make it cachable
# @cache
def rec(minutes_left, current_valve, active_valves, pressure_release):
    # print("rec()", minutes_left, current_valve, active_valves, pressure_release)
    if minutes_left < 3 and current_valve != "AA" and not is_active(current_valve, active_valves):
        return pressure_release + flow_rate[current_valve]
    elif minutes_left < 2:
        return pressure_release

    max = 0
    for next_valve in distances[current_valve]:
        cost = distances[current_valve][next_valve]

        if current_valve != "AA" and cost < minutes_left:

            # open valve and recurse
            pressure = rec(
                minutes_left - 1 - cost,
                next_valve,
                set_active(current_valve, active_valves),
                pressure_release + flow_rate[current_valve] * (minutes_left - 1 - cost),
            )
            if pressure > max:
                max = pressure
        elif cost + 1 < minutes_left:
            # recurse without opening valve
            pressure = rec(minutes_left - cost, next_valve, active_valves, pressure_release)
            if pressure > max:
                max = pressure
    # if max > 900:
    #    print(minutes_left, max)

    return max


print(rec(28, "AA", 0, 0))

# print(len(list(itertools.permutations(functioning_valves))))
print(distances)

# Caching holder ikke
# Tror vi må til med max (pos, min_left, active_valves)
# Da kan vi bygge opp nedenfra
# antallet unike kall blir da antall posisjoner*30*2^functioning_valves.
# Det skal bli noe sånt som 14745600 ved 30 min. Det fine er at antallet permutasjoner
# ikke blir mye større.
