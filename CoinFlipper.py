import random

def headsOrTails():
    result = random.randint(0,1)
    if result == 1:
        return 1
    else:
        return 0

def flip(n):
    for i in range(1,n+1):
        if headsOrTails() == 1:
            print("Toss " + str(i) + ": Tails")
        else:
            print("Toss " + str(i) + ": Heads")

flip(15)