doorid = 'ffykfhsq'
#doorid = 'abc'
import hashlib

hashed = []
index = 0

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
        result = hashlib.md5((doorid+str(index)).encode()).hexdigest()
        if valid(result):
            password += result[5]
            hashed.append(result)
        index+=1
    return password

def part2(doorid):
    global index
    password = ['-1','-1','-1','-1','-1','-1','-1','-1']
    result = doorid
    for h in hashed:
        if inbounds(h) and password[int(h[5])] == '-1':
            password[int(h[5])] = h[6]
    while '-1' in password:
        result = hashlib.md5((doorid+str(index)).encode()).hexdigest()
        if valid(result) and inbounds(result) and password[int(result[5])] == '-1':
            password[int(result[5])] = result[6]
        index+=1
    return ''.join(password)

print(part1(doorid))
print(part2(doorid))
