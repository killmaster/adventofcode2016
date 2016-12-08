import re
import collections

rule1 = re.compile(r'rect (?P<X>\d+)x(?P<Y>\d+)')
rule2 = re.compile(r'rotate (row|column) (x|y)=(?P<index>\d+) by (?P<amount>\d+)')

lines = open('input.txt').readlines()

display = [['.' for i in range(50)] for j in range(6)]

def pixels(display):
    return '\n'.join([''.join(['{}'.format(item) for item in row]) for row in display]).count('#')

def print_display():
    print('\n'.join([''.join(['{}'.format(item) for item in row]) for row in display]))


def draw_rect(x, y):
    for i in range(x):
        for j in range(y):
            display[j][i] = '#'

def rotate(l, n):
    return l[-n:] + l[:-n]

def rotate_row(index, amount):
    display[index] = rotate(display[index], amount)

def rotate_column(index, amount):
    column = [row[index] for row in display]
    column = rotate(column,amount)
    for i in range(len(display)):
        display[i][index] = column[i]

def parse(lines):
    for line in lines:
        if 'rect' in line:
            draw_rect(int(rule1.match(line).group('X')), int(rule1.match(line).group('Y')))
        elif 'row' in line:
            rotate_row(int(rule2.match(line).group('index')), int(rule2.match(line).group('amount')))
        elif 'column' in line:
            rotate_column(int(rule2.match(line).group('index')), int(rule2.match(line).group('amount')))

parse(lines)
print(pixels(display))
print_display()
