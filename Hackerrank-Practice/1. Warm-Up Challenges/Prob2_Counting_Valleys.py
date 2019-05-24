import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    up = 0
    down = 0
    ground = 0
    belowGround = False
    for items in s:
        #print items
        if items == "U":
            ground += 1
        else:
            ground -= 1

        if belowGround == False and ground < 0:
            valley += 1
            belowGround = True

        if ground >= 0:
            belowGround = False

    return valley


if __name__ == '__main__':
    print "Enter no of steps \n"
    n = int(raw_input())
    print "Enter the step types in U and D format \n"
    s = str(raw_input())
    #print len(s)
    if len(s) != n:
        print "Wrong input"
        exit()
    else:
        result = countingValleys(n, s)
        print result
