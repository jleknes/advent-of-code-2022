from functools import cache
import time, fileinput, re

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
blueprints = {}


def simulate():
    minutes_left = 24
    robots, resources = [0] * 4, [0] * 4
    robots[ORE] = 1

    while minutes_left > 0:
        # Hvis det er mulig å kjøpe en geode-robot, gjør det
        if resources[ORE] > 1 and resources[OBSIDIAN] > 6:
            resources[ORE] -= 2
            resources[OBSIDIAN] -= 7
            robots[GEODE] += 1
        minutes_left -= 1
        for i in range(len(robots)):
            resources[i] += robots[i]

    print(resources)


# simulate()


@cache
def rec(minutes_left, blueprint_id, ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian):

    #pruning? 
    # har vi noen heuristikker som kan si at denne metoden gir mindre utbytte enn beste kalkulerte mulighet så langt?

    if minutes_left == 1:
        #    if geode + geode_robots == 9:
        #        print(ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots)
        return geode_robots
    # må flyttes. mineralene kommer inn senere i prosessen.
    # ore += ore_robots
    # clay += clay_robots
    # obsidian += obsidian_robots
    # geode += geode_robots
    max_ore_robots = max(blueprints[blueprint_id][ORE],blueprints[blueprint_id][CLAY],blueprints[blueprint_id][OBSIDIAN][0],blueprints[blueprint_id][GEODE][0])
    max_clay_robots = blueprints[blueprint_id][OBSIDIAN][1]

    options = []
    if ore >= blueprints[blueprint_id][GEODE][0] and obsidian >= blueprints[blueprint_id][GEODE][1]:
        return rec(
            minutes_left - 1,
            blueprint_id,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots + 1,
            ore - blueprints[blueprint_id][GEODE][0] + ore_robots,
            clay + clay_robots,
            obsidian - blueprints[blueprint_id][GEODE][1] + obsidian_robots
        )+ geode_robots

    if ore >= blueprints[blueprint_id][OBSIDIAN][0] and clay >= blueprints[blueprint_id][OBSIDIAN][1]:
        options.append(
            rec(
                minutes_left - 1,
                blueprint_id,
                ore_robots,
                clay_robots,
                obsidian_robots + 1,
                geode_robots,
                ore - blueprints[blueprint_id][OBSIDIAN][0] + ore_robots,
                clay - blueprints[blueprint_id][OBSIDIAN][1] + clay_robots,
                obsidian + obsidian_robots,                
            )+ geode_robots
        )
    if ore >= blueprints[blueprint_id][CLAY] and clay_robots<max_clay_robots:
        options.append(
            rec(
                minutes_left - 1,
                blueprint_id,
                ore_robots,
                clay_robots + 1,
                obsidian_robots,
                geode_robots,
                ore - blueprints[blueprint_id][CLAY] + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots
            )+ geode_robots
        )
    if ore >= blueprints[blueprint_id][ORE] and ore_robots<max_ore_robots:
        options.append(
            rec(
                minutes_left - 1,
                blueprint_id,
                ore_robots + 1,
                clay_robots,
                obsidian_robots,
                geode_robots,
                ore - blueprints[blueprint_id][ORE] + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots
            )+ geode_robots
        )
    options.append(
        rec(
            minutes_left - 1,
            blueprint_id,
            ore_robots,
            clay_robots,
            obsidian_robots,
            geode_robots,
            ore + ore_robots,
            clay + clay_robots,
            obsidian + obsidian_robots
        )+ geode_robots
    )
    return max(options)


# robots, resources = [0] * 4, [0] * 4
# robots[ORE] = 1
start_time = time.time()
# print(rec(23, 1, 1, 0, 0, 0, 0, 0, 0, 0))
# print(rec(23, 2, 1, 0, 0, 0, 0, 0, 0, 0))
print("--- %s seconds ---" % (time.time() - start_time))


def read_blueprint(line):
    # rom for forbedring her.
    blueprint = {}
    blueprint[ORE] = int(re.findall(r"\d+", line)[1])
    blueprint[CLAY] = int(re.findall(r"\d+", line)[2])
    blueprint[OBSIDIAN] = (int(re.findall(r"\d+", line)[3]), int(re.findall(r"\d+", line)[4]))
    blueprint[GEODE] = (int(re.findall(r"\d+", line)[5]), int(re.findall(r"\d+", line)[6]))
    return blueprint

def read_input():
    blueprint_id = 0
    for line in fileinput.input():
        blueprint_id += 1
        blueprints[blueprint_id] = read_blueprint(line.strip())
    print(blueprints)


def solve_part_one():
    total_quality = 0
    for blueprint_id in blueprints.keys():
        print("processing blueprint id:", blueprint_id)
        geodes = rec(24, blueprint_id, 1, 0, 0, 0, 0, 0, 0)
        print(geodes)
        rec.cache_clear()
        total_quality += geodes * blueprint_id

    print(total_quality)  

def solve_part_two():   
    product = 1
    for blueprint_id in range(1, 4):
        print("processing blueprint id:", blueprint_id)
        geodes = rec(32, blueprint_id, 1, 0, 0, 0, 0, 0, 0)
        print(geodes)
        rec.cache_clear()
        product*=geodes
        print(product)


read_input()
start_time = time.time()
solve_part_one()
solve_part_two()
print("--- %s seconds ---" % (time.time() - start_time))
