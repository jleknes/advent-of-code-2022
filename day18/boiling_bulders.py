import fileinput
lava = set()
outside_air = set()

def read_input():
    for line in fileinput.input():
        x,y,z = list(map(int,line.strip().split(',')))
        lava.add((x,y,z))

# -1<x<20, -1<y<20, -1<z<20,
def get_adjacent_cubes(cube):
    x,y,z = cube
    adjacent = []
    for dx in range (-1,2):
        if dx!= 0 and x+dx>=-1 and x+dx<21:
            adjacent.append((x+dx,y,z))
    for dy in range (-1,2):
        if dy!= 0 and y+dy>=-1 and y+dy<21:
            adjacent.append((x,y+dy,z))
    for dz in range (-1,2):
        if dz!= 0 and z+dz>=-1 and z+dz<21:
            adjacent.append((x,y,z+dz))
    return adjacent


def solve_part_one():
    result = 0
    for cube in lava:
        cubes_to_test = get_adjacent_cubes(cube)
        for test in cubes_to_test:
            if not test in lava:
                result+=1
    print ("part one:",result)

#strategi for å finne air pockets: 3D BFS, start på utsiden av kuben
#finn alle kuber av luft på utsiden av kuben. Da vet vi at luft som ikke er en del av dette settet er en luftlomme

def find_outside_air():
    x,y,z = -1,-1,-1
    visited = set()
    queue = []
    visited.add((x,y,z))
    queue.append((x,y,z))
    while len(queue)>0:
        cube = queue.pop(0)
        for adjacent_cube in get_adjacent_cubes(cube):
            if not adjacent_cube in visited and adjacent_cube not in lava:
                queue.append(adjacent_cube)
                visited.add(adjacent_cube)
    outside_air.update(visited)

def solve_part_two():
    result = 0
    for cube in lava:
        cubes_to_test = get_adjacent_cubes(cube)
        for test in cubes_to_test:
            if test in outside_air:
                result+=1
    print ("part two:",result)

read_input()
solve_part_one()
find_outside_air()
solve_part_two()
