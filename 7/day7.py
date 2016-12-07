import re
import collections
#p1 = re.compile(r'(\w+)\[(\w+)\](\w+)')

with open('input.txt') as f:
    lines = f.read().splitlines()

def isPalindrome(word):
    return word == word[::-1]

def abba(word):
    index = 4
    while index < len(word)+1:
        if isPalindrome(word[index-4:index]) and collections.Counter(word[index-4:index]).most_common()[0][1] != 4:
            return True
        index += 1
    return False

def parse(line):
    hypernet = []
    nothypernet = []
    while '[' in line:
        nothypernet.append(line[:line.find('[')])
        line = line[line.find('[') + 1:]
        hypernet.append(line[:line.find(']')])
        line = line[line.find(']') + 1:]
    if len(line) > 0:
        nothypernet.append(line)
    return hypernet, nothypernet


def part1(lines):
    result = 0
    for line in lines:
        #hypernet = []
        #nothypernet = []
        hypernet_flag = False
        nothypernet_flag = False
        """while ']' in line:
            nothypernet.append(line[:line.find('[')])
            line = line[line.find('[') + 1:]
            hypernet.append(line[:line.find(']')])
            line = line[line.find(']') + 1:]
            if len(line) > 0:
                nothypernet.append(line)"""
        hypernet, nothypernet = parse(line)
        #print('hypernet: {}'.format(hypernet))
        #print('nothypernet: {}'.format(nothypernet))
        for c in hypernet:
            if abba(c):
                hypernet_flag = True
        if not hypernet_flag:
            for c in nothypernet:
                if abba(c):
                    nothypernet_flag = True
        if not hypernet_flag and nothypernet_flag:
            result += 1
    return result

def aba(word):
    index = 3
    result = []
    flag = False
    while index < len(word)+1:
        if isPalindrome(word[index-3:index]) and collections.Counter(word[index-3:index]).most_common()[0][1] < 3:
            result.append(word[index-3:index])
            flag = True
        index += 1
    if flag:
        return result
    return False

def bab(word, aba):
    #print('bab word: {}'.format(aba))
    index = 3
    tofind = aba[1] + aba[0] + aba[1]
    while index < len(word)+1:
        currentword = word[index-3:index]
        if currentword == tofind:
            #print('bab currentword: {}'.format(currentword))
            #print('bab tofind: {}'.format(tofind))
            return True
        index += 1
    return False

def part2(lines):
    result = 0
    for line in lines:
        found = False
        hypernet, nothypernet = parse(line)
        #print('hypernet: {}'.format(hypernet))
        #print('nothypernet: {}'.format(nothypernet))
        for c in nothypernet:
            temp = aba(c)
            if temp:
                for t in temp:
                    for h in hypernet:
                        if bab(h, t):
                            found = True
        if found:
            #print('found {}'.format(line))
            result += 1
    return result

print(part1(lines))
print(part2(lines))
