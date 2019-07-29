"""For M*N matrix total paths = (M+N-2)C(N-1)
 = (Factorial(M+N-2)/(Factorial(N-1)*Factorial(M-1))
 """
import math

def findPaths(m, n):
    paths = math.Factorial(m+n-2)/(math.Factorial(n-1)*math.Factorial(m-1))

    print (paths)

if __name__ == "__main__":
    print ("Enter dimensions of matrix")
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    print ("Dimensions are {} * {}".format(m,n))
    findPaths(m,n)
