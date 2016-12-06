import collections

with open('input.txt') as f:
    lines = f.read().splitlines()

horizontal_input = []
[horizontal_input.append([]) for x in range(len(lines[0]))]
for line in lines:
    index = 0
    for char in line:
        horizontal_input[index].append(line[index])
        index += 1

result = ''
result = result.join([''.join(collections.Counter(line).most_common()[0][0]) for line in horizontal_input])
print(result)
result2 = ''
result2 = result2.join([''.join(collections.Counter(line).most_common()[-1][0]) for line in horizontal_input])
print(result2)
