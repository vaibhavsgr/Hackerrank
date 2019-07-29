"""
Algorithm:
1) Start with start = 0, end = x,
2) Do following while start is smaller than or equal to end.
a) Compute mid as (start + end)/2
      b) compare mid*mid with x.
      c) If x is equal to mid*mid, return mid.
      d) If x is greater, do binary search between mid+1 and end.
        In this case, we also update ans (Note that we need floor).
      e) If x is smaller, do binary search between start and mid
"""
import math

def sqRoot(x):
    start = 1
    end = x/2

    while (start<=end):
        mid = (start+end)/2
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            end = mid-1
        elif mid*mid < x:
            start = mid+1
            ans = mid

    return ans

if __name__ == "__main__":
    print ("Enter n")
    n = int(input())
    print ("Floor Sq root of n")
    print (sqRoot(n))
