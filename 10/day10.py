import re
import collections

rule1 = re.compile(r'value (\d+) goes to (\w+ \d+)')
rule2 = re.compile(r'(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)')

lines = open('input.txt').readlines()

bots = collections.OrderedDict()

for line in lines:
    if rule1.match(line):
        botid = rule1.match(line).group(2)
        value = rule1.match(line).group(1)
        if botid in bots:
            if 'value1' in bots[botid]:
                bots[botid]['value2'] = value
        else:
            bots[botid] = {}
            bots[botid]['value1'] = value
    if rule2.match(line):
        botid = rule2.match(line).group(1)
        id1 = rule2.match(line).group(2)
        id2 = rule2.match(line).group(3)
        if botid not in bots:
            bots[botid] = {}
        bots[botid]['rule'] = []
        bots[botid]['rule'].append(id1)
        bots[botid]['rule'].append(id2)


        if id1.startswith('output') and id1 not in bots:
            bots[id1] = []
        if id2.startswith('output') and id2 not in bots:
            bots[id2] = []
        
        '''
        if rule2.match(line).group(2) == 'bot':
            bots[botid]['rule'].append(rule2.match(line).group(3))
        if rule2.match(line).group(4) == 'bot':
            bots[botid]['rule'].append(rule2.match(line).group(5))
        if rule2.match(line).group(2) == 'output':
            bots[botid]['rule'].append('output'.join(rule2.match(line).group(3)))
        if rule2.match(line).group(4) == 'output':
            bots[botid]['rule'].append('output'.join(rule2.match(line).group(5)))
        '''

def give(botid, value):
    if 'value1' in bots[botid]:
        bots[botid]['value2'] = value
    else:
        bots[botid]['value1'] = value

def part1(bots):
    while True:
        for k,v in bots.items():
            if 'value2' in v:
                values = sorted([int(v['value1']), int(v['value2'])])
                #print(v['rule'])
                if v['rule'][0].startswith('output'):
                    bots[v['rule'][0]].append(values[0])
                else:
                    give(v['rule'][0], values[0]) 
                if v['rule'][1].startswith('output'):
                    bots[v['rule'][1]].append(values[1])
                else:
                    give(v['rule'][1], values[1]) 
                if values == [17,61]:
                    return k

print(bots)
print(part1(bots))
print(bots['output 0'])
print(bots['output 1'])
print(bots['output 2'])
