import re

def solve(lines, part2 = None):
    discs = []
    rule = re.compile(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).')
    for line in lines:
        positions = int(rule.match(line).group(2))
        startpos = int(rule.match(line).group(4))
        discs.append((startpos, positions))
    if part2:
        discs.append((0,11))
    #print(discs)
    #print(range(len(discs)))
    timer = 0
    while True:
        result = [(discs[i][0] + timer + i) % discs[i][1] for i in range(len(discs))]
        #print(result)
        if len(set(result)) <= 1 and result[0] == 0:
            return timer-1
        timer += 1

if __name__ == '__main__':
    lines = open('input.txt').readlines()
    print(solve(lines))
    print(solve(lines, part2 = True))
