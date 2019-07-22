"Check if a given array can represent Preorder Traversal of Binary Search Tree"
"SOLUTION"
"""
1) Create an empty stack.
2) Initialize root as INT_MIN.
3) Do following for every element pre[i]
     a) If pre[i] is smaller than current root, return false.
     b) Keep removing elements from stack while pre[i] is greater
        then stack top. Make the last removed item as new root (to
        be compared next).
        At this point, pre[i] is greater than the removed root
        (That is why if we see a smaller element in step a), we
        return false)
     c) push pre[i] to stack (All elements in stack are in decreasing
        order)  """

def checkArrayforPOT(arr):
    root = -2**32
    st = []
    for _ in arr:
        if _ < root:
            return False
        while (len(arr) > 0 and arr[-1] < _):
            root = arr.pop()
        st.append(_)
    return True


if __name__ == "__main__":
    #print ("enter the size of the array")
    #n = int(input())
    #arr = []
    #print ("Enter the pre order traversal of the array")
    #for _ in range(n):
    #    arr.append(int(input().strip()))
    #arr = [40, 30, 35, 80, 100]
    arr = [40 , 30 , 35 , 20 ,  80 , 100]

    print (checkArrayforPOT(arr))
