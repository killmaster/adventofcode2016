from collections import deque
from functools import wraps
import time
import heapq
import math
import queue

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
    return wrapper

input_num = 1362

class State:
    def __init__(self, position, track, endposition):
        self.position = position
        self.track = track
        self.endposition = endposition

    def __repr__(self):
        return 'State({},{})'.format(self.position[0],self.position[1])

    def __str__(self):
        return 'State: {}, {}'.format(self.position[0],self.position[1])

    def __eq__(self, other):
        return  self.position == other.position

    def __hash__(self):
        return hash((self.position[0], self.position[1]))


class Node:
    def __init__(self, parent, state, f, g, h):
        self.parent = parent
        self.state = state
        self.f = f
        self.g = g
        self.h = h

    def __repr__(self):
        return (self.f, self.parent, self.state, self.g, self.h)

    def __str__(self):
        return '({}, {}, {}, {}, {})'.format(self.parent, self.state, self.f, self.g, self.h)

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.f < other.f

class Problem:
    def __init__(self, initialstate, nextstates, isgoal, h):
        self.initialstate = initialstate
        self.nextStates = nextstates
        self.isGoal = isgoal
        self.h = h

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def heuristic(state):
    (x1,y1) = state.position
    (x2,y2) = state.endposition
    return distance(state.position, state.endposition) + abs(x1-x2) + abs(y1-y2)
    #return int(distance(state.position, state.endposition))

def track(x, y, fav_num):
    number = x * x + 3 * x + 2 * x * y + y + y * y + fav_num
    return bin(number).count('1') % 2 == 0

def nextStates(state):
    result = []
    xpos,ypos = state.position
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        x = xpos + move[0]
        y = ypos + move[1]
        if x >= 0 and y >= 0:
            #print('({}, {})'.format(x,y))
            if state.track(x,y,input_num):
                result.append(State((x,y), state.track, state.endposition))
    return result

def isGoal(state):
    return state.position == state.endposition

#@timethis
def bfs(problem, part2=False):
    visited = set()
    frontier = deque()
    currentnode = Node(None, problem.initialstate, 0,0,0)
    frontier.append(currentnode)
    while frontier:
        currentnode = frontier.popleft()
        currentstate = currentnode.state
        if currentnode.f > 50 and part2:
            print(len(visited))
            return currentnode
        if problem.isGoal(currentstate):
            return currentnode
        visited.add(currentstate)
        for nextstate in problem.nextStates(currentstate):
            if nextstate not in visited:
                child = Node(currentnode, nextstate, currentnode.f+1,0,0)
                frontier.append(child)
    return currentnode

#@timethis
def astar(problem):
    visited = set()
    frontier = []
    currentcost = heuristic(problem.initialstate)
    currentnode = Node(None, problem.initialstate, currentcost, 0, 0)
    visited.add(problem.initialstate)
    heapq.heappush(frontier, (currentcost, currentnode))
    while frontier:
        currentnode = heapq.heappop(frontier)[1]
        currentstate = currentnode.state
        visited.add(currentstate)
        if problem.isGoal(currentstate):
            index = 0
            while currentnode.parent:
                print(currentnode.state)
                index += 1
                currentnode = currentnode.parent
            return index
        for successor in problem.nextStates(currentstate):
            if successor not in visited:
                temp_h = heuristic(successor)
                temp_cost = currentnode.g + 1
                f = temp_h
                successornode = Node(currentnode, successor, f, temp_cost, temp_h)
                heapq.heappush(frontier, (f, successornode))

if __name__ == '__main__':
    initialstate = State((1, 1), track, (31,39))
    part1problem = Problem(initialstate, nextStates, isGoal, 0)
    resultnode = astar(part1problem)
    print(resultnode)
    resultnode = bfs(part1problem)
    index = 0
    while resultnode.parent:
        print(resultnode.state)
        index += 1
        resultnode = resultnode.parent
    print(index)
    resultnode = bfs(part1problem, part2=True)
