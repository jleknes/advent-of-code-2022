
import sys,fileinput

jetstream = fileinput.input()[0].strip()

grid = [ ['.']*7 for i in range(5000)]

pieces = [[['X','X','X','X']],
[['.','X','.'],['X','X','X'],['.','X','.']],
[['.','.','X'],['.','.','X'],['X','X','X']],
[['X'],['X'],['X'],['X']],
[['X','X'],['X','X']]]


def collision (piece_index, y_pos, x_pos):
    if y_pos==len(grid)-1:
        return True
    if y_pos<2:
        return False
    piece = pieces[piece_index]
    for y in range(len(piece)):
        for x in range(len(piece[y])):
            #print (y_pos-y+1,x_pos+x)
            if piece[y][x]=='X' and grid[y_pos+y-len(piece)+2][x_pos+x]=='X':
                return True
    return False

def collision_right(piece_index, y_pos, x_pos):
    piece = pieces[piece_index]
    if x_pos+len(piece[0])==7:
        return True
    for y in range(len(piece)):
        for x in range(len(piece[y])):
            #print (y_pos-y+1,x_pos+x)
            if piece[y][x]=='X' and grid[y_pos+y-len(piece)+1][x_pos+x+1]=='X':
                return True
    return False

def collision_left(piece_index, y_pos, x_pos):
    piece = pieces[piece_index]
    if x_pos==0:
        return True
    for y in range(len(piece)):
        for x in range(len(piece[y])):
            #print (y_pos-y+1,x_pos+x)
            if piece[y][x]=='X' and grid[y_pos+y-len(piece)+1][x_pos+x-1]=='X':
                return True
    return False

def height():
    for y in range(len(grid)):
        if 'X' in grid[y]:
            return len(grid)-y
    return 0

def printpiece(piece_index):
    piece = pieces[piece_index]
    for y in range(len(piece)):
        for x in range(len(piece[y])):
            sys.stdout.write(piece[y][x])
        print()
    print()


def play_round(piece_index, jet_index):
    piece = pieces[piece_index]
    rest = False
    # x_pos representerer den delen av brikken som er lengst til venstre, 0-indeksert
    x_pos = 2
    # y_pos representerer den nederste delen av brikken
    # 0 er den nederste linja.
    y_pos = len(grid)-height()-4

    while (rest==False):
        # Kode for å avgjøre hva som skal skje når jet streamen dytter på en brikke
        if jetstream[jet_index]=='<' and not collision_left(piece_index,y_pos,x_pos):
            x_pos-=1
        elif jetstream[jet_index]=='>' and not collision_right(piece_index,y_pos,x_pos):
            x_pos+=1
        jet_index=(jet_index+1)%len(jetstream)
        

        if collision(piece_index,y_pos,x_pos):
            rest=True
        else:
            y_pos+=1
        

    for y in range(len(piece)):
        for x in range(len(piece[y])):
            if piece[y][x]=='X':
                grid[y_pos+y-len(piece)+1][x_pos+x]=piece[y][x]

    
    return jet_index

def printgrid():
    for y in range(len(grid)-height()-2, len(grid)):
        for x in range(len(grid[y])):
            sys.stdout.write(grid[y][x])
        print()
    print()

jet_index = 0
lastheight = 0
for i in range(2022):
    jet_index = play_round(i%5, jet_index)
print(height())


# Part two ble løst ved å finne mønster og regne ut
