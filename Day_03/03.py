# General Function
def gatherInput(file):       
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line[:-1])
    return lines


# part 1 functions
def part1():
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
                # if only 2 adjacent pairs, then score
                if len(adjLocations) == 2:
                    accum += score(adjLocations, lines)
            colctr += 1
        rowctr += 1
    print(accum)

# find the 2 numbers represented by a pair in locs, multiply them together
def score(locs, lines):
    sum = 1
    for pair in locs:
        sum *= findNum(pair, lines)
    return sum

# no bounds checking because I'm lazy and added a border of periods to my input
def checkNeighbors2(lines, row, col):
    adjLocations = []
    # check row above
    #if directly above is a digit, then above us is only one digit
    if lines[row - 1][col].isdigit():
        adjLocations.append((row - 1, col))
    #otherwise check the left/right knowing they're seperate numbers
    else:
        if lines[row - 1][col - 1].isdigit():
            adjLocations.append((row - 1, col - 1))
        if lines[row - 1][col + 1].isdigit():
            adjLocations.append((row - 1, col + 1))

    #check left/right
    if lines[row][col - 1].isdigit():
        adjLocations.append((row, col - 1))
    if lines[row][col + 1].isdigit():
        adjLocations.append((row, col + 1))
    
    #check below, if center below is digit, then only 1 digit beneath us
    if lines[row + 1][col].isdigit():
        adjLocations.append((row + 1, col))
    else:
        if lines[row + 1][col - 1].isdigit():
            adjLocations.append((row + 1, col - 1))
        if lines[row + 1][col + 1].isdigit():
            adjLocations.append((row + 1, col + 1))

    return adjLocations


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


part1()
part2()



"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola 
lift will take you up to the water source, but this is as far as he can bring 
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: 
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of 
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working 
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, 
but nobody can figure out which one. If you can add up all the part numbers in 
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of 
the engine. There are lots of numbers and symbols you don't really understand, 
but apparently any number adjacent to a symbol, even diagonally, is a "part 
number" and should be included in your sum. (Periods (.) do not count as a 
symbol.)

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

In this schematic, two numbers are not part numbers because they are not 
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number 
is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of 
the part numbers in the engine schematic?

Your puzzle answer was 544664.
"""

"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine 
springs to life, you jump in the closest gondola, finally ready to ascend to the 
water source.

You don't seem to be going very fast, though. Maybe something is still wrong? 
Fortunately, the gondola has a phone labeled "help", so you pick it up and the 
engineer answers.

Before you can explain the situation, she suggests that you look out the window. 
There stands the engineer, holding a phone in one hand and waving with the 
other. You're going so slowly that you haven't even left the station. You exit 
the gondola.

The missing part wasn't the only issue - one of the gears in the engine is 
wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its 
gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so 
that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears. The first is in the top left; it has 
part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the 
lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear 
because it is only adjacent to one part number.) Adding up all of the gear 
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 84495585.

Both parts of this puzzle are complete! They provide two gold stars: **
"""