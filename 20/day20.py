def part1(ranges, limit):
    ranges = sorted([list(map(int, r.rstrip().rsplit('-'))) for r in ranges], key=lambda r:r[0])
    top = 0
    for r in ranges:
        if r[0] <= top + 1:
            top = max(top,r[1])
        else:
            return top + 1
    return -1

def part2(ranges, limit):
    ranges = sorted([list(map(int, r.rstrip().rsplit('-'))) for r in ranges], key=lambda r:r[0])
    top = 0
    allowed = 0
    for r in ranges:
        if r[0] > top + 1:
            allowed += r[0] - top - 1
        top = max(r[1],top)
    allowed += limit - top
    return allowed

if __name__ == '__main__':
    puzzle_input = open('input.txt').readlines()
    #puzzle_input = open('input-test.txt').readlines()
    limit = 4294967295
    #limit = 9
    print(part1(puzzle_input, limit))
    print(part2(puzzle_input, limit))
