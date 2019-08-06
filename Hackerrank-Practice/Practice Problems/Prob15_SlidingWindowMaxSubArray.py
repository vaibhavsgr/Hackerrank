"""Use Max-Heap

1. Pick first k elements and create a max heap of size k.
2. Perform heapify and print the root element.
3. Store the next and last element from the array
4. Run a loop from k – 1 to n
    a. Replace the value of element which got out of the window with new
        element which came inside the window.
    b. Perform heapify.
    c. Print the root of the Heap.

Time Complexity: Time Complexity of steps 4(a) is O(k), 4(b) is O(Log(k)) and
                it is in a loop that runs (n – k + 1) times. Hence, the time
                complexity of the complete algorithm is O((k + Log(k)) * n) i.e.
                O(n * k).
"""

import heapq

def slidingWindowMaxSubArray(arr, k):
    i = 0
    j = k-1

    heap = arr[i:k]
    heapq._heapify_max(heap)

    # Print the maximum element from
    # the first window of size k
    print(heap[0], end =" ")
    last = arr[i]
    i+= 1
    j+= 1
    nexts = arr[j]

    # For every remaining element
    while j < n:

        # Add the next element of the window
        heap[heap.index(last)] = nexts

        # Heapify to get the maximum
        # of the current window
        heapq._heapify_max(heap)

        # Print the current maximum
        print(heap[0], end =" ")
        last = arr[i]
        i+= 1
        j+= 1
        if j < n:
            nexts = arr[j]

if __name__ == "__main__":
    n, k = 10, 3
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slidingWindowMaxSubArray(arr, k)
