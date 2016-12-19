import hashlib

class State:
    def __init__(self, position, hash, room, endposition):
        self.position = position
        self.room = room
        self.endposition = endposition
        self.hash = hash

    def __repr__(self):
        return 'State {}'.format(position)
    def __eq__(self, other):
        return self.position == other.position

class Node:
    def __init__(self, parent, state, f):
        self.parent = parent
        self.state = state
        self.f = f
    def __repr__(self):
        return (self.f, self.parent, self.state)

    def __str__(self):
        return '({}, {}, {})'.format(self.parent, self.state, self.f)

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

def isGoal(state):
    return state.position == state.endposition

def nextStates(state, current_hash):
    result = []
    xpos,ypos = state.position
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]




def get_hash(data):
    digest = hashlib.md5(data.encode()).hexdigest()
    return digest

if __name__ == '__main__':
    main()
