import random

def headsOrTails():
    result = random.randint(0,1)
    if result == 1:
        return "Tails"
    else:
        return "Heads"

def flip_and_print(n):
    for i in range(1,n+1):
        print("Toss " + str(i)+ ": " + headsOrTails())

def makeTable(n):
    resultTable = {}
    for i in range(1,n+1):
        resultTable[i] = headsOrTails()
    return resultTable