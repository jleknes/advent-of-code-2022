import sys, time

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

# (dy,dx)
moves = [(-1,0),(1,0),(0,-1),(0,1)]
check_tiles = ([(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)])
adjacent_tiles = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

length = 0
width = 0 
initial_positions = set()

def read_input():
    global length, width

    # Read the grid from standard input
    grid_str = sys.stdin.read()

    # Split the string into a list of rows
    grid_rows = grid_str.strip().split('\n')
    length = len(grid_rows)

    for row_index, row in enumerate(grid_rows):
        width = len(row)
        for col_index, col in enumerate(row):
            if col == '#':
                initial_positions.add((row_index, col_index))

def get_duplicates(lst):
    seen = set()
    duplicates = set()

    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return duplicates

# check if no elves are adjacent
def no_adjacent_elves(position, positions):
    no_adjacent = True
    for tile in adjacent_tiles:
        if (position[0]+tile[0],position[1]+tile[1]) in positions:
            no_adjacent = False
    return no_adjacent

def get_move(position, positions, first_direction):
    for i in range(4):        
        direction = (i+first_direction)%4
        proposed_move = (position[0]+moves[direction][0],position[1]+moves[direction][1])

        for j in range(len(check_tiles[direction])):
            pos = (position[0]+check_tiles[direction][j][0],position[1]+check_tiles[direction][j][1])
            if pos in positions:
                break
            elif j==len(check_tiles[direction])-1:
                return proposed_move
    return position

def print_grid(positions):
    min_y = min(map(lambda x: x[0], positions)) if min(map(lambda x: x[0], positions))<0 else 0
    max_y = max(map(lambda x: x[0], positions)) if max(map(lambda x: x[0], positions))>length else length
    min_x = min(map(lambda x: x[1], positions)) if min(map(lambda x: x[1], positions))<0 else 0
    max_x = max(map(lambda x: x[1], positions)) if max(map(lambda x: x[1], positions))>width else width
    
    for y in range(min_y, max_y):
        line = ""
        for x in range(min_x,max_x):
            if (y,x) in positions:
                line+="#"
            else:
                line+="."
        print(line)


def solve_part_one():
    positions = set(initial_positions)
    print_grid(positions)

    for i in range(10):
        proposed_moves = {}
        for elf in positions:
            if no_adjacent_elves(elf, positions):
                proposed_moves[elf] = elf
            else:
                proposed_moves[elf] = get_move(elf,positions, i%4)
        duplicate_moves = get_duplicates(list(proposed_moves.values()))
        positions = set()
        for key in proposed_moves:
            move = proposed_moves[key]
            if move not in duplicate_moves:
                positions.add(move)
            else:
                positions.add(key)
        print(f"After round: {i+1}")
        print_grid(positions)

    min_y, max_y = min(map(lambda x: x[0], positions)), max(map(lambda x: x[0], positions))
    min_x, max_x = min(map(lambda x: x[1], positions)), max(map(lambda x: x[1], positions))
    result = (max_y-min_y+1)*(max_x-min_x+1)-len(positions)
    print(f"part one: {result}")


def solve_part_two():
    positions = set(initial_positions)
    count = 0
    stable = False
    while not stable:
        proposed_moves = {}
        for elf in positions:
            if no_adjacent_elves(elf, positions):
                proposed_moves[elf] = elf
            else:
                proposed_moves[elf] = get_move(elf,positions, (count)%4)
        duplicate_moves = get_duplicates(list(proposed_moves.values()))

        positions = set()

        stable = True
        for key in proposed_moves:
            move = proposed_moves[key]
            if move not in duplicate_moves:
                positions.add(move)
                if key!=move:
                    stable = False
            else:
                positions.add(key)
                if key!=move:
                    stable = False

        print(f"After round: {count}")
        count+=1
    print(f"part two: {count}")

read_input()
print (width,length,initial_positions)
solve_part_one()
start_time = time.time()
solve_part_two()
print("--- %s seconds ---" % (time.time() - start_time))
