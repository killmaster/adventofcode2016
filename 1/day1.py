import math
orientation = 'N'
origin = [0,0]
origin2 = [0,0]
history = []
flag = False

def calc_distance(point):
    return int(math.fabs(point[0])+math.fabs(point[1]))

def turn_right():
    global orientation
    if orientation == 'N':
        orientation = 'E'
    elif orientation == 'E':
        orientation = 'S'
    elif orientation == 'S':
        orientation = 'W'
    else: orientation = 'N'

def turn_left():
    global orientation
    if orientation == 'N':
        orientation = 'W'
    elif orientation == 'W':
        orientation = 'S'
    elif orientation == 'S':
        orientation = 'E'
    else: orientation = 'N'

def move(distance):
    global orientation, origin
    multipliers = {
            'N': [0,1],
            'E': [1,0],
            'S': [0,-1],
            'W': [-1,0],
            }[orientation]
    origin[0] = origin[0] + distance * multipliers[0]
    origin[1] = origin[1] + distance * multipliers[1]

def move2(distance):
    global orientation, origin2, flag, history
    multipliers = {
            'N': [0,1],
            'E': [1,0],
            'S': [0,-1],
            'W': [-1,0],
            }[orientation]
    for i in range(distance):
        temp = (origin2[0] + multipliers[0], origin2[1] + multipliers[1])
        origin2[0] = origin2[0] + multipliers[0]
        origin2[1] = origin2[1] + multipliers[1]
        if temp in history and not flag:
            flag = True
            print(calc_distance(origin2))
            return
        history.append(temp)

f = open("input.txt", "r")

directions = f.readline().split(', ')

for direction in directions:
    if direction[0] == 'R':
        turn_right()
    elif direction[0] == 'L':
        turn_left()
    move(int(direction[1:]))
    move2(int(direction[1:]))

print(calc_distance(origin))
