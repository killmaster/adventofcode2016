line = open('input.txt').readline().strip()

def decompressor5000(line, decompressed = False):
    cont = 0
    while '(' in line:
        cont += line.find('(')
        line = line[line.find('('):]
        marker = line[1:line.find(')')].split('x')
        line = line[line.find(')') + 1:]
        if decompressed:
            cont += decompressor5000(line[:int(marker[0])], True) * int(marker[1])
        else:
            cont += len(line[:int(marker[0])]) * int(marker[1])
        line = line[int(marker[0]):]
    if len(line) > 0:
        cont += len(line)
    return cont

print(decompressor5000(line))
print(decompressor5000(line, decompressed = True))
