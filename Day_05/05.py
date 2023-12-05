import time

def makeEmptySeeds():
    seeds = {
        "seeds": [],
        "seed-to-soil map": [],
        "soil-to-fertilizer map": [],
        "fertilizer-to-water map": [],
        "water-to-light map": [],
        "light-to-temperature map": [],
        "temperature-to-humidity map": [],
        "humidity-to-location map": []
    }
    return seeds

def parseInput(openStr, seeds):
    with open(openStr) as f:
        currentKey = "\n"
        for line in f:
            if line != "\n":
                instr = line.split(":")[0]
                # check if we need to update which entry we're reading into
                if instr in seeds:
                    currentKey = instr
                # check for the seeds entry cuz its weird
                if currentKey == "seeds":
                    gatherSeeds(line, seeds)
                # otherwise, if we start with a digit, need to read into the dict
                if line[0].isdigit():
                    readInNums(line, currentKey, seeds)

def readInNums(line, currentKey, seeds):
    numSection = line.split()
    seeds[currentKey].append( [int(match) for match in numSection] )

def gatherSeeds(line, seeds):
    breakPoint = line.find(":")
    numSection = line[breakPoint+1:].split()
    seeds['seeds'] = [int(match) for match in numSection]

def translate(searchNum, seeds, dictStr):
    # destRange, srcRange, length
    for row in seeds[dictStr]:
        destRangeStart = row[0]
        srcRangeStart = row[1]
        length = row[2]
        srcRange = range(srcRangeStart, srcRangeStart + length)
        if searchNum in srcRange:
            # if at start of range, then 0
            numIn = searchNum - srcRangeStart
            return destRangeStart + numIn
    # if no match found, just return the number unmodified
    return searchNum

def seedLookups(seeds):
    locationNumbers = []
    for seedNum in seeds['seeds']:
        soilNum = translate(seedNum, seeds, "seed-to-soil map")
        fertNum = translate(soilNum, seeds, "soil-to-fertilizer map")
        waterNum = translate(fertNum, seeds, "fertilizer-to-water map")
        lightNum = translate(waterNum, seeds, "water-to-light map")
        tempNum = translate(lightNum, seeds, "light-to-temperature map")
        humidNum = translate(tempNum, seeds, "temperature-to-humidity map")
        locNum = translate(humidNum, seeds, "humidity-to-location map")
        locationNumbers.append(locNum)
    return (min(locationNumbers))

def changeSeedsRange(seeds):
    seeds["seeds"] = [(seeds["seeds"][i], seeds["seeds"][i + 1]) for i in range(0, len(seeds["seeds"]) - 1, 2)]
    seeds["seeds"] = merge_ranges(seeds["seeds"])

def seedLookups2(seeds):    
    #hold the ranges as they're translated
    translatePairs = {
        'seeds': seeds['seeds'],
        'soil': [],
        'fertilizer': [],
        'water': [],
        'light': [],
        'temperature': [],
        'humidity': [],
        'location': []
    }

    #translate seeds
    print("seeds")
    for seedPair in translatePairs['seeds']:
        translate2(seedPair, seeds, "seed-to-soil map", translatePairs, 'seeds', 'soil')
    print("soil")
    print(translatePairs['soil'])
    for soilPair in translatePairs['soil']:
        translate2(soilPair, seeds, "soil-to-fertilizer map", translatePairs, 'soil', 'fertilizer')
    print("fert")
    for fertPair in translatePairs['fertilizer']:
        translate2(fertPair, seeds, "fertilizer-to-water map", translatePairs, 'fertilizer', 'water')
    print("water")
    for waterPair in translatePairs['water']:
        translate2(waterPair, seeds, "water-to-light map", translatePairs, 'water', 'light')
    print("light")
    print(translatePairs['light'])
    for lightPair in translatePairs['light']:
        #print(lightPair)
        translate2(lightPair, seeds, "light-to-temperature map", translatePairs, 'light', 'temperature')
    print("temp")
    for tempPair in translatePairs['temperature']:
        translate2(tempPair, seeds, "temperature-to-humidity map", translatePairs, 'temperature', 'humidity')
    print("humidity")
    for humidPair in translatePairs['humidity']:
        translate2(humidPair, seeds, "humidity-to-location map", translatePairs, 'humidity', 'location')

    minLocationNum = float('inf')
    print("loc")
    for locPair in translatePairs['location']:
        if locPair[0] < minLocationNum:
            minLocationNum = locPair[0]

    return minLocationNum

def translate2(searchPair, seeds, dictStr, translatePairs, srcString, destString):
    # destRange, srcRange, length
    for row in seeds[dictStr]:
        destRangeStart = row[0]
        srcRangeStart = row[1]
        length = row[2]

        # what if they fully overlap
        if searchPair[0] >= srcRangeStart and searchPair[0] + searchPair[1] <= srcRangeStart + length:
            translatePairs[destString].append((searchPair[0] + destRangeStart, searchPair[1]))
        # what if they partially overlap
        elif searchPair[0] <= srcRangeStart + length and searchPair[0] + searchPair[1] >= srcRangeStart:
            overlapStart = max(searchPair[0], srcRangeStart)
            overlapEnd = min(searchPair[0] + searchPair[1], srcRangeStart + length)
            overlapRange = overlapEnd - overlapStart
            noOverlapLow = [-1,-1]
            noOverlapHigh = [-1,-1]

            # find start of low overlap
            if searchPair[0] < overlapStart:
                noOverlapLow[0] = searchPair[0]
                noOverlapLow[1] = overlapStart - noOverlapLow[0]
            if overlapEnd < searchPair[0] + searchPair[1]:
                # gets the size of the past the range
                noOverlapHigh[1] = searchPair[0] + searchPair[1] - overlapEnd
                noOverlapHigh[0] = overlapEnd + 1
            if noOverlapLow != [-1, -1]:
                translatePairs[srcString].append((noOverlapLow[0], noOverlapLow[1]))
            if noOverlapHigh != [-1, -1]:
                translatePairs[srcString].append((noOverlapHigh[0], noOverlapHigh[1]))
            translatePairs[destString].append((overlapStart, overlapRange))
        # otherwise, no overlap, carryon
        else:
            pass

    # if no match found, just return the number unmodified
    translatePairs[destString].append(searchPair)

def merge_ranges(pairs):
    # Sort the pairs based on the start values
    sorted_pairs = sorted(pairs, key=lambda x: x[0])

    merged_ranges = []
    current_range = None

    for start, count in sorted_pairs:
        if current_range is None or start > current_range[0] + current_range[1]:
            # If no overlap or the start is after the current range, create a new range
            current_range = (start, count)
            merged_ranges.append(current_range)
        else:
            # If there is an overlap, extend the current range
            current_range = (current_range[0], max(current_range[1], start + count - current_range[0]))

    return merged_ranges



def part1():
    print("Part 1")
    seeds = makeEmptySeeds()
    parseInput("input.txt", seeds)
    print (seedLookups(seeds))


def part2():
    print("Part 2")
    seeds = makeEmptySeeds()
    parseInput("testinput.txt", seeds)
    changeSeedsRange(seeds)
    print(seeds)

    print(seedLookups2(seeds))

startTime = time.time()
part1()
endTime = time.time()
elapsed = (endTime - startTime) * 1000
print("Part one ran in " + str(elapsed) + " ms")

startTime = time.time()
part2()
endTime = time.time()
elapsed = (endTime - startTime) * 1000
print("Part two ran in " + str(elapsed) + " ms")

