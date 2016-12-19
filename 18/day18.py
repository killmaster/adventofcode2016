def solve(puzzle_input, rows):
    map = {
    "..." : '.',
    "..^" : '^',
    ".^." : '.',
    ".^^" : '^',
    "^.." : '^',
    "^.^" : '.',
    "^^." : '^',
    "^^^" : '.',
    }
    tiles = []
    result = ''
    temp = ''
    reading = puzzle_input
    tiles.append(reading)
    safes = 0
    while rows > 1:
        idx = 0
        while idx < len(reading):
            if idx == 0:
                temp = '.' + reading[idx] + reading[idx+1]
            elif idx == len(reading) - 1:
                temp = reading[idx-1] + reading[idx] + '.'
            else:
                temp = reading[idx-1] + reading[idx] + reading[idx+1]
            if map[temp] == '.':
                safes += 1
            result+=map[temp]
            idx += 1
        tiles.append(result)
        reading = result
        result = ''
        rows -=1
    [print(''.join(tile)) for tile in tiles]
    #for tile in tiles:
    #    for t in tile:
    #        if t == '.':
    #            safes += 1
    safes = sum(x.count('.') for x in tiles)
    return safes

if __name__ == '__main__':
    #puzzle_input = '..^^.'
    #puzzle_input = '.^^.^.^^^^'
    puzzle_input = '.^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^'
    print(solve(puzzle_input,40))
    print(solve(puzzle_input,400000))
