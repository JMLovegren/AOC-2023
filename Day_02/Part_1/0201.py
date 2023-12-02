import re

#Determine which games would have been possible if the bag had been loaded with 
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the 
# IDs of those games?

MAXRED = 12
MAXGREEN = 13
MAXBLUE = 14

with open('input.txt') as f:
    accum = 0
    ctr = 0
    for line in f:
        ctr += 1
        pattern = r'(\d+)\s+red'
        redNums = re.findall(pattern, line)
        redNums = [int(match) for match in redNums]

        pattern = r'(\d+)\s+green'
        greenNums = re.findall(pattern, line)
        greenNums = [int(match) for match in greenNums]

        pattern = r'(\d+)\s+blue'
        blueNums = re.findall(pattern, line)
        blueNums = [int(match) for match in blueNums]
        if max(redNums) <= MAXRED and max(greenNums) <= MAXGREEN and max(blueNums) <= MAXBLUE:
            accum += ctr
    print (accum)
