import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    #new_string = (n/len(s))*s + s[:n%len(s)]
    #for items in new_string:
    #    if items == 'a':
    #        count +=1
    for items in s:
        if items == 'a':
            count += 1
    result = count*(n/len(s))
    for items in s[:n%len(s)]:
        if items == 'a':
            result += 1
    #result = count*(n/len(s))
    return result


if __name__ == '__main__':
    print "Enter the string"
    s = str(raw_input())
    print "Enter the repetitions of the above string to be considered"
    n = int(raw_input())
    result = repeatedString(s, n)
    print result
