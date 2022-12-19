import fileinput, time 
from functools import cache

flow_rate = {}
paths = {}
functioning_valves = []

def readinput():
    for line in fileinput.input():
        valve = line[6:8]
        rate = line[line.index("=") + 1 : line.index(";")]
        tunnels = [path.strip() for path in line[line.index("valve") + 6 :].strip().split(",")]
        flow_rate[valve] = int(rate)
        paths[valve] = tunnels
        if flow_rate[valve] > 0:
            functioning_valves.append(valve)


# bitstring
def is_active(valve, code):
    # a bit expensive
    valvepos = functioning_valves.index(valve)
    return (code >> valvepos) & 1


def set_active(valve, code):
    # a bit expensive
    valvepos = functioning_valves.index(valve)
    return code | 1 << valvepos

def pressure_release(active_valves):
    pressure = 0
    for valve in functioning_valves:
        if is_active(valve, active_valves):
            pressure+=flow_rate[valve]
    return pressure

@cache
def solve_part_one(minutes_left, active_valves, human_pos):
    released_pressure = pressure_release(active_valves)
    if minutes_left==1:
        return released_pressure
    else:
        options = []
        if human_pos in functioning_valves:
            options.append(solve_part_one(minutes_left-1,set_active(human_pos,active_valves),human_pos)+released_pressure)

        for human_path in paths[human_pos]:
            options.append(solve_part_one(minutes_left-1,active_valves,human_path)+released_pressure)
        return max(options)

@cache
def solve_part_two(minutes_left, active_valves, human_pos, elephant_pos):
    released_pressure = pressure_release(active_valves)
    if minutes_left==1:
        return released_pressure
    else:
        options = []
        for human_path in paths[human_pos]+[human_pos]:
            for elephant_path in paths[elephant_pos]+[elephant_pos]:
                if human_path==human_pos and human_pos in functioning_valves:
                    options.append(solve_part_two(minutes_left-1,set_active(human_path,active_valves),human_path,elephant_path)+released_pressure)
                if elephant_path==elephant_pos and elephant_pos in functioning_valves:
                    options.append(solve_part_two(minutes_left-1,set_active(elephant_path,active_valves),human_path,elephant_path)+released_pressure)
                if human_path==human_pos and human_pos in functioning_valves and elephant_path==elephant_pos and elephant_pos in functioning_valves:
                    options.append(solve_part_two(minutes_left-1,set_active(elephant_path,set_active(human_path,active_valves)),human_path,elephant_path)+released_pressure)
                options.append(solve_part_two(minutes_left-1,active_valves,human_path,elephant_path)+released_pressure)
        return max(options)
                

readinput()
start_time = time.time()
print(solve_part_one(30, 0, 'AA'))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(solve_part_two(26, 0, 'AA', 'AA'))
print("--- %s seconds ---" % (time.time() - start_time))

