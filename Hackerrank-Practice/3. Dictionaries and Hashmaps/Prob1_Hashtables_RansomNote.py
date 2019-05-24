import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    count = 0
    #if len(note) > len(magazine):
    #    return "No"
    #else:
    #    for words in note:
    #        if words in magazine:
    #            magazine.remove(words)
    #            count += 1
    #        else:
    #            return "No"
    if (Counter(note) - Counter(magazine)) == {}:
        return "Yes"
    else:
        return "No"

    #if count == len(note):
    #    return 'Yes'


if __name__ == '__main__':
    print "Enter length of magazine and length of note"
    mn = raw_input().split()
    m = int(mn[0])
    n = int(mn[1])
    print "Enter magazine words"
    magazine = raw_input().rstrip().split()
    print "Enter note words"
    note = raw_input().rstrip().split()
    res = checkMagazine(magazine, note)
    print res
