doorid = 'ffykfhsq'
#doorid = 'abc'
import hashlib
import random
import sys

hashed = []
index = 0

def hacking_in_progress(password, hashed, index):
    if index % 30000 == 0:
        sys.stdout.write('password: {}\tcracking hash: {}\r'.format(''.join(password),hashed))
        sys.stdout.flush()

def valid(h):
    if h.startswith('00000'):
        return True
    else:
        return False

def inbounds(result):
    if result[5].isdigit() and int(result[5]) < 8 and int(result[5]) >= 0:
        return True
    else:
        return False

def part1(doorid):
    global index
    password = ''
    result = doorid
    while len(password) < 8:
        hacking_in_progress(password, result, index)
        result = hashlib.md5((doorid+str(index)).encode()).hexdigest()
        if valid(result):
            password += result[5]
            hashed.append(result)
        index+=1
    return password

def part2(doorid):
    global index
    password = ['_','_','_','_','_','_','_','_']
    result = doorid
    for h in hashed:
        hacking_in_progress(password,result,index)
        if inbounds(h) and password[int(h[5])] == '_':
            password[int(h[5])] = h[6]
    while '_' in password:
        hacking_in_progress(password, result, index)
        result = hashlib.md5((doorid+str(index)).encode()).hexdigest()
        if valid(result) and inbounds(result) and password[int(result[5])] == '_':
            password[int(result[5])] = result[6]
        index+=1
    return ''.join(password)

part1 = part1(doorid)
sys.stdout.write('password: {}\r'.format(part1))
sys.stdout.flush()
print('\npassword 1: {}\r'.format(part1))
part2 = part2(doorid)
sys.stdout.write('password: {}\r'.format(part2))
sys.stdout.flush()
print('\npassword 2: {}\r'.format(part2))
