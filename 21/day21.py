from itertools import permutations

def part2(lines, puzzle_input):
    for perm in permutations(puzzle_input):
        if part1(lines, perm) == puzzle_input:
            return ''.join(perm)

def rot_right(l,n):
    return l[-n:] + l[:-n]

def rot_left(l,n):
    return l[n:] + l[:n]

def part1(lines, puzzle_input):
    result = list(puzzle_input)
    for line in lines:
        splitted = line.split()
        digs = [int(x) for x in splitted if x.isdigit()]
        if line.startswith('swap position'):
            x, y = digs
            result[x], result[y] = result[y], result[x]
        elif line.startswith('swap letter'):
            x, y = splitted[2], splitted[-1]
            i, j = result.index(x), result.index(y)
            result[i], result[j] = result[j], result[i]
        elif line.startswith('rotate left'):
            x = digs[0]
            result = rot_left(result, x)
        elif line.startswith('rotate right'):
            x = digs[0]
            result = rot_right(result, x)
        elif line.startswith('rotate based'):
            c = splitted[-1]
            i = result.index(c)
            i += (i>=4) + 1
            i = i % len(result)
            result = rot_right(result, i)
        elif line.startswith('reverse'):
            x, y = digs
            result[x: y+1] = result[x: y+1][::-1]
        else:
            x,y = digs
            a = result.pop(x)
            result = result[:y]+[a]+result[y:]
        #print('instruction:{} result:{}'.format(line,''.join(result)))
    return ''.join(result)

if __name__ == '__main__':
    lines = open('input.txt').readlines()
    puzzle_input = 'abcdefgh'
    print(part1(lines, puzzle_input))
    puzzle_input2 = 'fbgdceah'
    print(part2(lines, puzzle_input2))
