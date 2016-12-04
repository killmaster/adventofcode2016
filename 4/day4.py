with open('input.txt','r') as f:
    lines = f.read().splitlines()

result = 0

import re
import collections
import string
p1 = re.compile(r'(?P<name>[a-zA-Z0-9\-]+)-(?P<id>\d+)\[(?P<check>\w+)\]')

def caesar(sectorid):
    alphabet = string.ascii_lowercase
    pos = sectorid % len(alphabet)
    return str.maketrans(alphabet, alphabet[pos:] + alphabet[:pos])

for line in lines:
    name = p1.match(line).group('name')
    sectorid = int(p1.match(line).group('id'))
    check = p1.match(line).group('check')
    tops = [(-n,c) for c,n in collections.Counter(name.replace('-','')).most_common()]
    ranked = ''.join(c for n,c in sorted(tops))
    if ranked.startswith(check):
        decyphered = name.translate(caesar(sectorid))
        if 'north' in decyphered:
            print(decyphered, sectorid)
        result += sectorid

print(result)

