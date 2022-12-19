from enum import Enum

ORE= 0
CLAY= 1
OBSIDIAN= 2
GEODE= 3

def simulate():
    minutes_left = 24
    robots, resources = [0]*4, [0]*4
    robots[ORE] = 1

    while minutes_left>0:
        #Hvis det er mulig å kjøpe en geode-robot, gjør det
        if (resources[ORE]>1 and resources[OBSIDIAN]>6):
            resources[ORE]-=2
            resources[OBSIDIAN]-=7
            robots[GEODE]+=1
        minutes_left-=1
        for i in range(len(robots)):
            resources[i]+=robots[i]
         
    
    print(resources)

simulate()

