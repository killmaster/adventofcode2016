with open('input.txt','r') as f:
    lines = f.read().splitlines()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [['E','E','1','E','E'],
           ['E','2','3','4','E'],
           ['5','6','7','8','9'],
           ['E','A','B','C','E'],
           ['E','E','D','E','E']]
position = [1,1]
position2 = [2,0]
print(matrix2[2][0])

def part1(lines, position):
    result = []
    for line in lines:
        for c in line:
            move = {
                    'U': (-1,0),
                    'D': (1,0),
                    'R': (0,1),
                    'L': (0,-1),
                    }[c]
            position[0] += move[0]
            position[1] += move[1]
            if position[0] < 0:
                position[0] = 0
            if position[1] < 0:
                position[1] = 0
            if position[0] > 2:
                position[0] = 2
            if position[1] > 2:
                position[1] = 2
        result.append(matrix[position[0]][position[1]])
    return result

def part2(lines,position):
    result = []
    for line in lines:
        for c in line:
            move = {
                    'U': (-1,0),
                    'D': (1,0),
                    'R': (0,1),
                    'L': (0,-1),
                    }[c]
            temp = [position[0]+move[0],position[1]+move[1]]
            if temp[0] < 0:
                temp[0] = 0
            if temp[0] > 4:
                temp[0] = 4
            if temp[1] < 0:
                temp[1] = 0
            if temp[1] > 4:
                temp[1] = 4
            if matrix2[temp[0]][temp[1]] != 'E':
                position[0] = temp[0]
                position[1] = temp[1]
        result.append(matrix2[position[0]][position[1]])
    return result
                

print(part1(lines, position))
print(part2(lines, position2))

