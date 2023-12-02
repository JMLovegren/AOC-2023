import re

#Determine which games would have been possible if the bag had been loaded with 
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the 
# IDs of those games?

with open('input.txt') as f:
    accum = 0
    for line in f:
        pattern = r'(\d+)\s+red'
        redNums = re.findall(pattern, line)
        redNums = [int(match) for match in redNums]

        pattern = r'(\d+)\s+green'
        greenNums = re.findall(pattern, line)
        greenNums = [int(match) for match in greenNums]

        pattern = r'(\d+)\s+blue'
        blueNums = re.findall(pattern, line)
        blueNums = [int(match) for match in blueNums]
        
        accum += max(redNums) * max(greenNums) * max(blueNums)

    print (accum)
