

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # Case 1: if all characters are same number of times then
    # Condition 1: "values.count(values[0]) == len(values)"

    # Case 2: if (all-1) characters are same number of times and one chracater is atleast
    # one more than (all-1) character's frequency then
    # Condition 2: "values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1"

    # Case 3: if (all-1) character's frequency is same, and one character occurs only once then
    # Condition 3: "values.count(values[-1]) == len(values) - 1 and values[0] == 1
    
    freq = Counter(s)
    values = list(freq.values())
    values.sort()
    print values

    if values.count(values[0]) == len(values) or (values.count(values[0]) == len(values) - 1 and values[-1] - values[-2] == 1) or (values.count(values[-1]) == len(values) - 1 and values[0] == 1):
        return 'YES'
    else:
        return 'NO'



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter string"
    s = raw_input()
    result = isValid(s)
    print result
    #fptr.write(result + '\n')
    #fptr.close()
