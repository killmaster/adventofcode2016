import hashlib
import sys
import re
from itertools import count
from itertools import takewhile

def hash(salt, index):
    password = salt + str(index)
    result = hashlib.md5(password.encode()).hexdigest()
    return result

def hash2016(salt, index):
    password = salt + str(index)
    result = hash(salt, index)
    for i in range(2016):
        result = hashlib.md5(result.encode()).hexdigest()
    return result

def quintuple(hashes, ch):
    quint = ch * 5
    for h in hashes:
        if h.find(quint) != -1:
            return True
    return False

def cracker(salt, hash_func):
    find3 = re.compile(r'(.)\1{2,}')
    #find5 = re.compile(r'(.)\1{4,}')
    hashes = [hash_func(salt, i) for i in range(1001)]
    found = 0
    idx = 0
    while found < 64:
        current = find3.search(hashes.pop(0))
        if current and quintuple(hashes, current.group(1)):
            found += 1
        idx += 1
        hashes.append(hash_func(salt, idx+len(hashes)))
    return idx-1

if __name__ == '__main__':
    #print(cracker('abc', hash))
    #print(cracker('yjdafjpo', hash))
    #print(cracker('abc', hash2016))
    print(cracker('yjdafjpo', hash2016))
