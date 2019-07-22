def checkParanthesis(st):
    stack = []
    for c in st():
        if (c == "(" or c == "{" or c == "["):
            stack.push(c)
        elif c == ")" and stack[len(stack)-1] == ")" or c == "}" and stack[len(stack)-1] == "}" or c == "]" and stack[len(stack)-1] == "]" :
            stack.pop(c)
        else:
            flag = 1

    if flag == 1 or len(stack)>0:
        print ("Invalid")
    else:
        print ("Valid")

if __name__ == "__main__":
    print ("Enter Paranthesis to be checked")
    st = input()
    checkParanthesis(st)
