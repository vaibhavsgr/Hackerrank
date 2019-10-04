def findDay(d, m, y):
    ### 1 - Monday, 7 - SUnday
    t = [0,3,2,5,0,3,
         5,1,4,6,2,4]

    y -= m<3
    day = ( y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7
    return day

if __name__ ==  "__main__":
    print ("Enter the date in dd mm yy")
    d,m,y = input().split(" ")
    print (findDay(int(d), int(m), int(y)))
