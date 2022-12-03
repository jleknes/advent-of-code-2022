import fileinput

def priority(item):
    if (item.isupper()):
        return ord(item)-ord('A')+27
    else:
        return ord(item)-ord('a')+1

def rucksack(line):
    compartment_size = int(len(line)/2)
    compartment1 = set(line[0:compartment_size])
    compartment2 = set(line[-compartment_size:])
    item = compartment1.intersection(compartment2).pop()
    return priority(item)
    #return 0

def badge(lines):
    item = set.intersection(set(lines[0]),set(lines[1]),set(lines[2])).pop()
    return priority(item)

def part_two():
    sum = 0
    cnt = 0
    lines = []
    for line in fileinput.input():
        cnt+=1
        lines.append(line.strip())
        if (cnt==3):
            sum+=badge(lines)
            cnt=0
            lines = []
    print (sum)


def part_one():
    sum = 0
    for line in fileinput.input():
        sum+=rucksack(line.strip())
    print (sum)

part_two()