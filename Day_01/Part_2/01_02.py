numDict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
numList = ["zero", "one", "two", "three", "four", 
           "five", "six", "seven", "eight", "nine"]

with open('input.txt') as f:
    accum = 0
    for line in f:
        firstNum = -1
        lastNum = -1
        firstDigitPos = -1
        lastDigitPos = -1
        posCtr = -1
        for thing in line:
            posCtr += 1
            if thing.isdigit():
                lastNum = int (thing)
                lastDigitPos = posCtr
                if firstNum == -1:
                    firstNum = int (thing)
                    firstDigitPos = posCtr
        
        # edge case for no digits in string. Set to end of string
        if firstDigitPos == -1:
            firstDigitPos = posCtr
            lastDigitPos = 0

        if firstDigitPos != 0:
            # find any lower string representations
            firstSubStr = line [0:firstDigitPos]
            firstSubstrPos = firstDigitPos
            for num in numList:
                x = firstSubStr.find(num)
                if x > -1 and x < firstSubstrPos:
                    firstSubstrPos = x
                    firstStringNum = numDict[num]
            if firstSubstrPos < firstDigitPos:
                firstNum = firstStringNum


        if lastDigitPos != posCtr - 1: # -1 cuz it's also looping on \n
            # find any higher string representations
            lastSubStr = line[lastDigitPos:posCtr]
            lastSubStrPos = 0
            lastStringNum = -1
            for num in numList:
                # rfind finds LAST occurence of substring
                x = lastSubStr.rfind(num)
                if x > -1 and x > lastSubStrPos:
                    lastSubStrPos = x
                    lastStringNum = numDict[num]
            if lastStringNum > -1:
                lastNum = lastStringNum

        accum += firstNum * 10 + lastNum

    print("The total is " +  str(accum))
