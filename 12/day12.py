lines = open('input.txt').readlines()

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0,}
def part1(lines, registers):
    line = 0
    while line < len(lines):
        flag = False
        instruction = lines[line].split()
        if instruction[0] == 'cpy':
            try:
                registers[instruction[2]] = int(instruction[1])
            except:
                registers[instruction[2]] = registers[instruction[1]]
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        elif instruction[0] == 'dec':
            registers[instruction[1]] -= 1
        elif instruction[0] == 'jnz':
            try:
                value = registers[instruction[1]]
            except KeyError:
                value = int(instruction[1])
            if value != 0:
                flag = True
                line += int(instruction[2])
                continue
        line+=1
    return registers['a']

print(part1(lines,registers))
registers['c'] = 1
print(part1(lines,registers))
