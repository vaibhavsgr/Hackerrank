def sumAtKLevel(st, k):
    level = -1
    s = 0
    print (st)
    for ch in st:
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1
        elif level == k:
            s += ord(ch) - ord('0')

    print ("The result is ")
    print (s)

if __name__ == "__main__":
    st1 = '(0(5(6()())(4()(9()())))(7(1()())(3()())))'
    k1 = 2
    st2 = '(8(3(2()())(6(5()())()))(5(10()())(7(13()())())))'
    k2 = 3
    sumAtKLevel(st1, k1)
    sumAtKLevel(st2, k2)
