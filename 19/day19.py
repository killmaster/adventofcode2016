import collections
import math

def power_bit_length(x):
    return 2 ** int(math.log(x, 2))

def part1(value):
    return 2 * (value - power_bit_length(value)) + 1

def part2afterpattern(value):
    start = 1
    while start * 3 < value:
        start *= 3
    return value - start

def part2(value):
    elfs = [elf+1 for elf in range(value)]
    stealing_elf = 0
    while len(elfs) > 1:
        if stealing_elf > len(elfs):
            stealing_elf = 0
        #print(elfs)
        stonlen_from = elfs.pop((stealing_elf + int(len(elfs)/2)) % int(len(elfs)))
        #print('{} {} {}'.format(stealing_elf, len(elfs), stonlen_from))
        #print(stonlen_from)
        stealing_elf += 1

    return elfs.pop()


if __name__ == '__main__':
    value = 3014603
    #value = 5
    print(part1(value))
    print(part2afterpattern(value))
