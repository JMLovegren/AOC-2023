import re

def solve():
    with open('input.txt') as f:
        accum = 0
        for line in f:
            maxRed = findMax(line, 'red')
            maxGreen = findMax(line, 'green')
            maxBlue = findMax(line, 'blue')
            accum += maxRed * maxGreen * maxBlue

        print (accum)

def findMax(line, color):
    pattern = rf'(\d+)\s+{color}'
    numStrings = re.findall(pattern, line)
    numList = [int(match) for match in numStrings]
    return max(numList)

solve()