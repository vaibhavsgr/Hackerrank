def longIncSubsequence(arr, n):
    "arr = 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15"
    "LIS = 0, 2, 6, 9, 11, 15"
    sub = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[j]<arr[i]:
                sub[i] = sub[j] + 1

    return sub




if __name__ == "__main__":
    print ("Enter the size of the array")
    arr= []
    n = int(input().strip())
    print ("Enter the array elements")
    for _ in range(n):
        arr.append(int(input().strip()))
    res = longIncSubsequence(arr, n)
    print (res)
