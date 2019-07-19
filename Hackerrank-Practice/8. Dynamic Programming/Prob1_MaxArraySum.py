import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    #2 1 5 8 4
    #subets are = [2,5,4], [2,5], [2,4], [2,8], [1,8], [1,4], [5,4]
    dp = []
    dp.append(arr[0])
    dp.append(arr(1))
    ans = max(dp)

    for _ in arr[2:]:
        dp.append(max(max(arr[-2]+_, _), ans)
        ans = max(ans, dp[-1])

    return ans


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print ("Enter size of array")
    n = int(input())
    print ()"Enter the array elements")
    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    print res
    #fptr.write(str(res) + '\n')
    #fptr.close()
