#Coin flip simulator

import random

def coinFlip(numFlips):

    heads = 0;
    tails = 0;

    while numFlips > 0:
        if (random.randint(0,1) == 0):
            heads += 1
            numFlips = numFlips - 1
        else:
            tails += 1
            numFlips = numFlips - 1

    print "Heads: ", heads, "Tails: ", tails

coinFlip(4728)
