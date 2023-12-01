with open('input.txt') as f:
    accum = 0
    for line in f:
        firstNum = -1
        lastNum = -1
        for thing in line:
            if thing.isdigit():
                lastNum = int (thing)
                if firstNum == -1:
                    firstNum = int (thing)
        accum += firstNum * 10 + lastNum
    print ("The total is ", accum)