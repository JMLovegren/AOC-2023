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

def seedLookups2(seeds):
    locationNumbers = []
    for seedPair in seeds['seeds']:
        print("starting " + str(seedPair))
        ctr = seedPair[0]
        while ctr <= seedPair[0] + seedPair[1]:
            soilNum = translate(ctr, seeds, "seed-to-soil map")
            fertNum = translate(soilNum, seeds, "soil-to-fertilizer map")
            waterNum = translate(fertNum, seeds, "fertilizer-to-water map")
            lightNum = translate(waterNum, seeds, "water-to-light map")
            tempNum = translate(lightNum, seeds, "light-to-temperature map")
            humidNum = translate(tempNum, seeds, "temperature-to-humidity map")
            locNum = translate(humidNum, seeds, "humidity-to-location map")
            locationNumbers.append(locNum)
            ctr += 1
    return (min(locationNumbers))

def part1():
    print("Part 1")
    seeds = makeEmptySeeds()
    parseInput("input.txt", seeds)
    print (seedLookups(seeds))


def part2():
    print("Part 2")
    seeds = makeEmptySeeds()
    parseInput("input.txt", seeds)
    changeSeedsRange(seeds)
    print(seedLookups2(seeds))

part1()

part2()

