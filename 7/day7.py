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
    while ']' in line:
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
    while index < len(word)+1:
        if isPalindrome(word[index-3:index]) and collections.Counter(word[index-3:index]).most_common()[0][1] != 2:
            return word[index-3:index]
        index += 1
    return False

def bab(word, aba):
    index = 3
    while index < len(word)+1:
        if isPalindrome(word[index-3:index]) and collections.Counter(word[index-3:index]).most_common()[0][1] != 2 and word[index-3:index] != aba:
print(part1(lines))
