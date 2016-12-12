'''
*******************NOTE*********************
    This code is totally untested since
        I solved this one by hand.
        This should work but it'll
        take a long long time to do so
********************************************
'''


'''
elevator limit is 2
elevator must have a RTG or microchip to move
elevator always stops between floors
'''

#microchips are positive, generators are negative
promethium, cobalt, curium, ruthenium, plutonium = 1, 2, 3, 4, 5

floors = {1: [-promethium, promethium],
          2: [-cobalt, -curium, -ruthenium, -plutonium],
          3: [cobalt, curium, ruthenium, plutonium],
          4: [],
          }


'''
so it seems this is gonna be a BFS so lets get some lists going
'''
from collections import deque
from itertools import combinations
import copy

'''
a state is a pair (elevator_floor, floors)
'''
class Node:
    def __init__(self, parent, state, cost):
        self.parent = parent
        self.state = state
        self.cost = cost

    def __repr__(self):
        return str(self.state)
        
frontier = deque()
explored = []

def final(node):
    return node.state[0] == 4 and node.state[1][1] == node.state[1][2] == node.state[1][3] == []

def valid(floors):
    result = [] 
    for k, v in floors.items():
        if not v or v[0] > 0:
            result.append(True)
        else:
            result.append(all(-i in v for i in v if i > 0))
    return all(result)

def adjacentElevators(elevator, floors):
    if elevator == 1:
        return [2]
    if elevator == 4:
        return [3]
    if not floors[elevator-1]:
        return [elevator+1]
    return [elevator-1, elevator+1]

def nextMoves(state):
    result = []
    elevator = state[0]
    floors = state[1]
    moves = []
    for item in floors[elevator]:
        moves.append(item)
    [moves.append(list(combination)) for combination in combinations(floors[elevator],2)]
    nextelevators = adjacentElevators(elevator, floors)
    for nextelevator in nextelevators:
        for move in moves:
            nextfloors = copy.deepcopy(floors)
            if isinstance(move, list):
                nextfloors[nextelevator].extend(move)
                [nextfloors[elevator].remove(item) for item in move]
            else:
                nextfloors[nextelevator].append(move)
                nextfloors[elevator].remove(move)
            nextfloors[nextelevator] = sorted(nextfloors[nextelevator])
            if valid(nextfloors):
                result.append((nextelevator, nextfloors))
    return result
    
def bfs(floors):
    global frontier
    global explored
    distance = 0
    result = []
    node = Node(None,(1,floors),0)
    if final(node):
        return node
    frontier.append(node)
    while frontier:
        node = frontier.popleft()
        explored.append(node.state)
        if node.cost != distance:
            distance = node.cost
            print(distance)
        for action in nextMoves(node.state):
            child = Node(node,action, node.cost+1)
            if child.state not in explored and child not in frontier:
                if final(child):
                    print(child.cost)
                    result.append(child.cost)
                frontier.append(child)

def bfs2(floors):
    visited = []
    queue = deque()
    node = Node(None,(1,floors),0)
    queue.append(node)
    distance = 0
    while queue:
        current = queue.popleft()
        visited.append(current)
        if current.cost != distance:
            distance = current.cost
            print(distance)
        for next in nextMoves(current.state):
            node = Node(current,next,current.cost+1)
            if node not in visited and node not in queue:
                queue.append(node)
            if final(node):
                print(node.cost)

#bfs(floors)
bfs2(floors)


  
