import fileinput

results = {}
calculations = {}

def read_input():
    for line in fileinput.input():
        defines = line[0:4]
        if line[6:].strip().isnumeric():
            results[defines] = int(line[6:].strip())
        else:
            calculations[defines] = line[6:].strip()

            

    print(results,calculations)

def solve_part_one():
    while 'root' in calculations:
        for calculation in calculations:
            part1 = calculation[0:4]
            part2 = calculation[6:]
            if part1 in results and part2 in results:
                print (part1,part2)
 
read_input()
solve_part_one()