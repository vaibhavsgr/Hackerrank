"""
A number is called as a Jumping Number if all adjacent digits in it differ by 1.
The difference between 9 and 0 is not considered as 1.
All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not

Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101"""

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, n):
        self.q.append(n)

    def dequeue(self):
        return self.q.pop(0)

    def is_empty(self):
        return self.q==[]

st = []

def breadthFirstSearch(n, limit):
    Q = Queue()
    Q.enqueue(n)

    while(not Q.is_empty()):
        n = Q.dequeue()
        if n <= limit:
            print (str(n) + " ")
            st.append(n)
            last_digit = n % 10

            #if last_digit is 0, append last digit only
            if last_digit == 0:
                Q.enqueue(n*10 + last_digit+1)

            #if last_digit is 9, append first digit only
            elif last_digit == 9:
                Q.enqueue(n*10 + last_digit-1)

            else:
                Q.enqueue(n*10 + last_digit-1)
                Q.enqueue(n*10 + last_digit+1)

    #return Q

if __name__ == "__main__":
    print ("Enter the range")
    limit = int(input())
    #print (str(0), end =' ')
    #n = 40
    for n in range(10):
        breadthFirstSearch(n, limit)
    print st
