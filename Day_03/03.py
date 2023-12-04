
# General Function
def gatherInput(file):       
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line[:-1])
    return lines


# part 1 functions
def part1redo():
    lines = gatherInput("input.txt")
    lineCtr = 0
    accum = 0
    for line in lines:
        colCtr = 0
        lineLen = len(line)
        while colCtr < lineLen:
            if line[colCtr].isdigit():
                numLen = findNumLen(line, colCtr)
                if checkNeighbors(lines, lineCtr, colCtr, numLen):
                    accum += int(line[colCtr:colCtr + numLen])
                colCtr += numLen
            else:
                colCtr += 1
        lineCtr += 1
    print (accum)

def checkNeighbors(lines, row, colStart, numLen):
    ctr = 0
    
    while ctr < numLen:
        adjCol = colStart + ctr

        # check row above
        if not lines[row - 1][adjCol - 1].isdigit() and lines[row - 1][adjCol - 1] != '.':
            return True
        if not lines[row - 1][adjCol].isdigit() and lines[row - 1][adjCol] != '.':
            return True
        if not lines[row - 1][adjCol + 1].isdigit() and lines[row - 1][adjCol + 1] != '.':
            return True
        
        #check left/right
        if not lines[row][adjCol - 1].isdigit() and lines[row][adjCol - 1] != '.':
            return True
        if not lines[row][adjCol + 1].isdigit() and lines[row][adjCol + 1] != '.':
            return True
        
        #check below
        if not lines[row + 1][adjCol - 1].isdigit() and lines[row + 1][adjCol - 1] != '.':
            return True
        if not lines[row + 1][adjCol].isdigit() and lines[row + 1][adjCol] != '.':
            return True
        if not lines[row + 1][adjCol + 1].isdigit() and lines[row + 1][adjCol + 1] != '.':
            return True
        ctr += 1
    return False

def findNumLen(line, ctr):
    numLen = 1
    while line[ctr + 1].isdigit():
        numLen += 1
        ctr += 1
    return numLen
    


# part 2 function
def part2():
    lines = gatherInput("input.txt")
    accum = 0
    rowctr = 0
    for line in lines:
        colctr = 0
        while colctr < len(line):
            if lines[rowctr][colctr] == '*':
                # find the adjacent coordinates that have a digit in them
                adjLocations = checkNeighbors2(lines, rowctr, colctr)
                # prune that list to find if it has exactly 2 neighbors
                accum += prune(adjLocations, lines)
            colctr += 1
        rowctr += 1
    print(accum)

"""
This is where my problem likely is cuz my brain sorta just shat the bed on how
to solve this. 

The idea for this functinon, take a list of coordinates, find out if those
coordinates mark the locations for exactly 2 adjacent nubers, and return 
those numbers multiplied by each other. 

if there are 1 or 3 or more numbers adjacent, return 1

@locs - a list of pairs representing the row, col coordinate of a digit
@lines - a 2d list of the input
"""
def prune(locs, lines):
    # make a list of the row coordinates
    yCoordinate = []
    for pair in locs:
        if pair[0] not in yCoordinate:
            yCoordinate.append(pair[0])

    """
    case where on same line 
    123*456

    or 

    ...*...
    123.456
    """
    # hit if there's only 1 y coordinate and 2 pairs
    if len(yCoordinate) == 1 and len(locs) == 2:
        # find the full numbers from that point
        firstNum = findNum(locs[0], lines)
        lastNum = findNum(locs[1], lines)
        return firstNum * lastNum

    # otherwise, if there are are only digits on 2 rows
    elif len(yCoordinate) == 2:
        """
        This is where the real ridiculusness starts. The idea through this 
        section is to find out if there is gap in numbers or multiple
        adjacent

        for example

        3.2
        .*1

        would have an x coordinate seperated by more than 1 in the first row, 
        and wouldrepresent 3 different numbers

        321
        .*1

        would have all its adjacent numbers be represented in 2 groups,
        and would pass
        """
        # make lists of the x coordinates on each of the 2 lines
        x1co = []
        x2co = []
        for pair in locs:
            if pair[0] == yCoordinate[0]:
                x1co.append(pair[1])
            elif pair[0] == yCoordinate[1]:
                x2co.append(pair[1])

        # if both have no gaps
        if check_difference_by_one(x1co) and check_difference_by_one(x2co):
            # find what those digits fully represent
            firstNum = findNum(locs[0], lines)
            lastNum = findNum(locs[len(locs) - 1], lines)
            return firstNum * lastNum
        else:
            print("caught an edge case")

    return 0

# helper i found online to makesure list of numbers increments by 1
def check_difference_by_one(numbers):
    numbers.sort()
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) != 1:
            return False
    return True


# check backwards and forwards to find start of number, return full number
def findNum(pair, lines):
    colCtr = pair[1]
    row = pair[0]
    while lines[row][colCtr - 1].isdigit():
        colCtr -= 1
    # now have a ctr to the beginning
    first = colCtr
    while lines[row][colCtr + 1].isdigit():
        colCtr += 1
    # and ctr to end
    last = colCtr
    return int(lines[pair[0]][first:last + 1])

# check each of eight neighbors for digits, return a list of coordinates
# that do
def checkNeighbors2(lines, row, col):
    adjLocations = []

    # check row above
    if lines[row - 1][col - 1].isdigit():
        adjLocations.append((row - 1, col - 1))
    if lines[row - 1][col].isdigit():
        adjLocations.append((row - 1, col))
    if lines[row - 1][col + 1].isdigit():
        adjLocations.append((row - 1, col + 1))

    
    #check left/right
    if lines[row][col - 1].isdigit():
        adjLocations.append((row, col - 1))
    if lines[row][col + 1].isdigit():
        adjLocations.append((row, col + 1))
    
    #check below
    if lines[row + 1][col - 1].isdigit():
        adjLocations.append((row + 1, col - 1))
    if lines[row + 1][col].isdigit():
        adjLocations.append((row + 1, col))
    if lines[row + 1][col + 1].isdigit():
        adjLocations.append((row + 1, col + 1))

    return adjLocations


#part1redo()
part2()

# 77799141 is too low
# 88138311 is too high
# 10339170


"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 544664.


"""