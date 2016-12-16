def unfold(data):
    second = data[::-1]
    second = [str(abs(int(i)-1)) for i in second]
    result = data + '0' + ''.join(second)
    return result

def checksum(data, length):
    digest = data
    while len(digest) < length:
        digest = unfold(digest)
    digest = digest[0:length]
    while True:
        temp = []
        i = 0
        while i <= len(digest)-2:
            if digest[i] == digest[i+1]:
                temp.append('1')
            else:
                temp.append('0')
            i += 2
        if len(temp) % 2 == 1:
            return ''.join(temp)
        else:
            digest = ''.join(temp)

if __name__ == '__main__':
    puzzle_input = '10010000000110000'
    puzzle_length = 272
    testing = False
    if testing:
        test_input = '10000'
        test_length = 20
        test_result = checksum(test_input, test_length)
        print(test_result)
    else:
        result = checksum(puzzle_input, puzzle_length)
        print(result)
        result = checksum(puzzle_input, 35651584)
        print(result)
