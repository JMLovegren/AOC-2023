MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

import re

def solve():
    with open('input.txt') as f:
        accum = 0
        ctr = 0
        for line in f:
            ctr += 1
            maxRed = findMax(line, 'red')
            maxGreen = findMax(line, 'green')
            maxBlue = findMax(line, 'blue')
            if maxRed <= MAXRED and maxGreen <= MAXGREEN and maxBlue <=MAXBLUE:
                accum += ctr
        print (accum)

def findMax(line, color):
    pattern = rf'(\d+)\s+{color}'
    numStrings = re.findall(pattern, line)
    numList = [int(match) for match in numStrings]
    return max(numList)

solve()
