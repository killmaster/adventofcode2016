import re
import collections
p1 = re.compile(r'(?P<first>\w+)\[(?P<second>\w+)\](?P<third>\w+)')

with open('input-test.txt') as f:
    lines = f.read().splitlines()

def isPalindrome(word):
    print(word)
    return word == word[::-1]

def abba(word):
    index = 4
    while index < len(word):
        if isPalindrome(word[index-4:index]) and collections.Counter(word[index-4:index]).most_common()[0][1] != 4:
            return True
        index += 1
    return False

def part1(lines):
    result = 0
    for line in lines:
        first = p1.match(line).group('first')
        #print(first)
        second = p1.match(line).group('second')
        #print(second)
        third = p1.match(line).group('third')
        #print(third)
        if abba(first) or abba(third) and not abba(second):
            result += 1
    return result

print(part1(lines))
